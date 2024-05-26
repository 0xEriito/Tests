from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import random

# Define the grid size and colors
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Colors
COLORS = [
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
    (1, 1, 0, 1),
    (1, 0.65, 0, 1),
    (0.5, 0, 0.5, 1),
    (0, 1, 1, 1)
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

class TetrisWidget(Widget):
    def __init__(self, **kwargs):
        super(TetrisWidget, self).__init__(**kwargs)
        self.init_game()

        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def init_game(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.score = 0
        self.current_tetrimino = self.new_tetrimino()
        self.next_tetrimino = self.new_tetrimino()
        self.game_over = False
        self.current_pos = [GRID_WIDTH // 2, 0]
        self.fall_time = 0.5
        self.time_passed = 0
        self.paused = False

    def new_tetrimino(self):
        return [random.choice(SHAPES), random.randint(1, len(COLORS) - 1)]

    def rotate_tetrimino(self):
        new_shape = list(zip(*self.current_tetrimino[0][::-1]))
        if self.valid_position(new_shape, self.current_pos):
            self.current_tetrimino[0] = new_shape

    def valid_position(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if x + off_x < 0 or x + off_x >= GRID_WIDTH or y + off_y >= GRID_HEIGHT:
                        return False
                    if y + off_y >= 0 and self.grid[y + off_y][x + off_x]:
                        return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT - 1, -1, -1):
            if 0 not in self.grid[y]:
                lines_cleared += 1
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.score += lines_cleared ** 2

    def draw_grid(self):
        self.canvas.clear()
        with self.canvas:
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    if self.grid[y][x]:
                        Color(*COLORS[self.grid[y][x]])
                        Rectangle(pos=(x * GRID_SIZE, y * GRID_SIZE), size=(GRID_SIZE, GRID_SIZE))

            for x in range(GRID_WIDTH):
                Color(0.5, 0.5, 0.5, 1)
                Rectangle(pos=(x * GRID_SIZE, 0), size=(1, self.height))
            for y in range(GRID_HEIGHT):
                Color(0.5, 0.5, 0.5, 1)
                Rectangle(pos=(0, y * GRID_SIZE), size=(self.width, 1))

    def draw_tetrimino(self, shape, offset):
        off_x, off_y = offset
        with self.canvas:
            for y, row in enumerate(shape):
                for x, cell in enumerate(row):
                    if cell:
                        Color(*COLORS[self.current_tetrimino[1]])
                        Rectangle(pos=((x + off_x) * GRID_SIZE, (y + off_y) * GRID_SIZE), size=(GRID_SIZE, GRID_SIZE))

    def update(self, dt):
        if self.paused:
            return

        self.time_passed += dt
        self.draw_grid()
        self.draw_tetrimino(self.current_tetrimino[0], self.current_pos)

        if self.game_over:
            return

        if self.time_passed >= self.fall_time:
            self.time_passed = 0
            if self.valid_position(self.current_tetrimino[0], (self.current_pos[0], self.current_pos[1] + 1)):
                self.current_pos[1] += 1
            else:
                for y, row in enumerate(self.current_tetrimino[0]):
                    for x, cell in enumerate(row):
                        if cell:
                            self.grid[self.current_pos[1] + y][self.current_pos[0] + x] = self.current_tetrimino[1]
                self.current_tetrimino = self.next_tetrimino
                self.next_tetrimino = self.new_tetrimino()
                self.current_pos = [GRID_WIDTH // 2, 0]
                if not self.valid_position(self.current_tetrimino[0], self.current_pos):
                    self.game_over = True
                self.clear_lines()

    def on_touch_down(self, touch):
        if self.paused:
            return

        if touch.x < self.width / 3:
            if self.valid_position(self.current_tetrimino[0], (self.current_pos[0] - 1, self.current_pos[1])):
                self.current_pos[0] -= 1
        elif touch.x > self.width * 2 / 3:
            if self.valid_position(self.current_tetrimino[0], (self.current_pos[0] + 1, self.current_pos[1])):
                self.current_pos[0] += 1
        else:
            self.rotate_tetrimino()
        self.draw_grid()
        self.draw_tetrimino(self.current_tetrimino[0], self.current_pos)

class PauseMenu(FloatLayout):
    def __init__(self, game_widget, **kwargs):
        super(PauseMenu, self).__init__(**kwargs)
        self.game_widget = game_widget

        resume_button = Button(text="Resume", size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.6})
        resume_button.bind(on_release=self.resume_game)
        self.add_widget(resume_button)

        restart_button = Button(text="Restart", size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.4})
        restart_button.bind(on_release=self.restart_game)
        self.add_widget(restart_button)

        quit_button = Button(text="Quit to Main Menu", size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.2})
        quit_button.bind(on_release=self.quit_to_main_menu)
        self.add_widget(quit_button)

    def resume_game(self, instance):
        self.game_widget.paused = False
        self.game_widget.parent.remove_widget(self)

    def restart_game(self, instance):
        self.game_widget.init_game()
        self.game_widget.parent.remove_widget(self)

    def quit_to_main_menu(self, instance):
        app = App.get_running_app()
        app.root.current = 'main_menu'
        self.game_widget.parent.remove_widget(self)

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.previous_scores = Label(text="Previous Scores:\nNone", size_hint=(1, 0.7))
        layout.add_widget(self.previous_scores)

        start_button = Button(text="Start", size_hint=(1, 0.15))
        start_button.bind(on_release=self.start_game)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game_screen'

    def update_scores(self, scores):
        self.previous_scores.text = "Previous Scores:\n" + "\n".join(map(str, scores))

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = TetrisWidget()
        self.add_widget(self.game)

        pause_button = Button(text="||", size_hint=(0.1, 0.1), pos_hint={'x': 0.9, 'y': 0.9})
        pause_button.bind(on_release=self.pause_game)
        self.add_widget(pause_button)

    def pause_game(self, instance):
        self.game.paused = True
        pause_menu = PauseMenu(self.game)
        self.add_widget(pause_menu)

class TetrisApp(App):
    def build(self):
        self.title = "Tetris"
        self.screen_manager = ScreenManager()

        self.main_menu = MainMenu(name='main_menu')
        self.screen_manager.add_widget(self.main_menu)

        self.game_screen = GameScreen(name='game_screen')
        self.screen_manager.add_widget(self.game_screen)

        return self.screen_manager

    def on_stop(self):
        # Save the current score before quitting
        if hasattr(self.game_screen.game, 'score'):
            score = self.game_screen.game.score
            # Add code here to save the score to a file or database
            # For now, just print it
            print(f"Final score: {score}")

if __name__ == '__main__':
    TetrisApp().run()
