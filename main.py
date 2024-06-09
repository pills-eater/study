import pygame
pygame.init()
W = 750
H = 500
win = pygame.display.set_mode((W, H))
orientations = ['U', 'L', 'R', 'D']
DRILLER = 'Driller'
SELLER = 'Seller'
COLORMACHINE = 'Colormachine'
BELT = 'Belt'
SPLITTER2 = '2 ways Splitter'       # влево вправо
SPLITTER3 = '3 ways Splitter'       # влево вверх вправо
L_SPLITTER = 'Left side Splitter'   # влево вверх
R_SPLITTER = 'Right side Splitter'  # вправо вверх
FPS = 15
RED = 'Red'
GREEN = 'Green'
BLUE = 'Blue'


clock = pygame.time.Clock()


def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    return img


class Board:
    def __init__(self):
        self.cl_size = 51
        self.cl_w = 15
        self.cl_h = 10
        self.contains = {}
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0],
            [0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 21, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0],
            [0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 0, 0],
            [0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0],
            [0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.red = load_img("textures/red.png")
        self.green = load_img("textures/green.png")
        self.blue = load_img("textures/blue.png")
        self.turbo1 = load_img("textures/turbo1.png")
        self.turbo2 = load_img("textures/turbo2.png")
        self.turbo3 = load_img("textures/turbo3.png")
        self.turbo4 = load_img("textures/turbo4.png")
        self.u_color = load_img("textures/ucolor.png")
        self.l_color = load_img("textures/lcolor.png")
        self.r_color = load_img("textures/rcolor.png")
        self.d_color = load_img("textures/dcolor.png")
        self.u_belt = load_img("textures/ubelt.png")
        self.l_belt = load_img("textures/lbelt.png")
        self.r_belt = load_img("textures/rbelt.png")
        self.d_belt = load_img("textures/dbelt.png")

    def render(self):
        for i in range(self.cl_h):
            for j in range(self.cl_w):
                if self.board[i][j] == 23 or self.board[i][j] == 27 or self.board[i][j] == 31:
                    win.blit(self.turbo1, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 24 or self.board[i][j] == 28 or self.board[i][j] == 32:
                    win.blit(self.turbo2, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 25 or self.board[i][j] == 29 or self.board[i][j] == 33:
                    win.blit(self.turbo3, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 26 or self.board[i][j] == 30 or self.board[i][j] == 34:
                    win.blit(self.turbo4, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 5:
                    win.blit(self.u_color, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 6:
                    win.blit(self.l_color, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 7:
                    win.blit(self.r_color, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 8:
                    win.blit(self.d_color, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 9:
                    win.blit(self.u_belt, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 10:
                    win.blit(self.l_belt, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 11:
                    win.blit(self.r_belt, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 12:
                    win.blit(self.d_belt, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 20:
                    win.blit(self.red, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 21:
                    win.blit(self.green, (j * self.cl_size, i * self.cl_size))
                if self.board[i][j] == 22:
                    win.blit(self.blue, (j * self.cl_size, i * self.cl_size))

# -----------Библиотеки----------- #


class MachineLib:
    def __init__(self):
        self.lib = {
            'Driller': {
                'cost': 0,
                'sQuantity': 5,
                'opTime': 10,
                'desc': 'Добывает базовые краски, медленный и ограниченный.',
                'type': 'basic',
                },
            'Colormachine': {
                'cost': 0,
                'sQuantity': 3,
                'opTime': 2,
                'desc': 'Изменяет краску, увеличивая её цену',
                'type': 'basic'
                },
            'Seller': {
                'cost': 0,
                'sQuantity': 1,
                'opTime': 1,
                'desc': 'Продаёт готовый продукт',
                'type': 'basic'
            }
        }

class MaterialLib:
    def __init__(self):
        self.lib = {
            'Green': {
                'cost': 50,
                'type': 'basic',
                'desc': 'Зелёная краска, не дорогая и не слишком дешёвая.'
        },
            'Red': {
                'cost': 20,
                'type': 'basic',
                'desc': 'Красная краска, дешёвая, но при надобной обработке может стать весьма ценной.'
            },
            'Blue': {
                'cost': 100,
                'type': 'basic',
                'desc': 'Синяя краска, дорогая, но в начале почти не пригождается.'
            }
    }


# -----------Машины----------- #
class ClsMachine:
    def __init__(self, machine, x, y, orientation, dropx, dropy):
        self.type = machine
        self.x = x
        self.y = y
        self.orientation = orientation
        self.cost = MachineLib.lib[self.type]['cost']
        self.listedBlueprint = []
        self.splitCumulative = [0, 0, 0]
        self.splitOutput = [0, 0, 0]
        self.splitSetting = None
        self.splitTurn = 0
        self.dropx = dropx
        self.dropy = dropy

    def orientation(self):
        if self.orientation == orientations[0]:
            self.dropx = board.cl_w
            self.dropy = board.cl_h - 1
        elif self.orientation == orientations[1]:
            self.dropx = board.cl_w - 1
            self.dropy = board.cl_h
        elif self.orientation == orientations[2]:
            self.dropx = board.cl_w + 1
            self.dropy = board.cl_h
        elif self.orientation == orientations[3]:
            self.dropx = board.cl_w
            self.dropy = board.cl_h + 1


class Player:
    def inter(self, board):
        keys = pygame.key.get_pressed()
        self.contains = {}
        self.m_pos_x = pygame.mouse.get_pos()[0]
        self.m_pos_y = pygame.mouse.get_pos()[1]
        self.cls_m = ClsMachine(DRILLER, self.m_pos_x, self.m_pos_y, orientations[0], board.cl_w, board.cl_h - 1)
        # self.cls_m = ClsMachine(DRILLER, board.board[self.m_pos_x // board.cl_size], board.board[self.m_pos_y // board.cl_size], orientations[0], board.cl_w, board.cl_h - 1)

        if keys[pygame.K_q] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 20:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 3
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[0]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 23:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]

            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 24:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 25:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 26:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] -= 3

        elif keys[pygame.K_q] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 21:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 6
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[0]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size][1] -= 1
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 27:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 28:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 29:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 30:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] -= 3

        elif keys[pygame.K_q] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 22:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 9
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[0]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 31:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 32:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 33:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] += 1
            self.cls_m.type = DRILLER
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
            for i in range(MachineLib.lib[self.cls_m.type]['opTime']):
                count = 0
                count += i
                if count == MachineLib.lib[self.cls_m.type]['opTime']:
                    pass
        elif keys[pygame.K_c] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 34:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] -= 3

        elif keys[pygame.K_w]:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 5
            self.cls_m.type = COLORMACHINE
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[0]
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 5:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 6
            self.cls_m.type = COLORMACHINE
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[1]
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 6:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 7
            self.cls_m.type = COLORMACHINE
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[2]
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 7:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 8
            self.cls_m.type = COLORMACHINE
            self.cls_m.cost = MachineLib.lib[self.cls_m.type]['cost']
            self.cls_m.orientation = orientations[3]
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 8:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 5
        elif keys[pygame.K_1]:
            self.cls_m.type = BELT
            self.cls_m.orientation = orientations[0]

            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 9
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 9:
            self.cls_m.type = BELT
            self.cls_m.orientation = orientations[1]

            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 10
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 10:
            self.cls_m.type = BELT
            self.cls_m.orientation = orientations[2]
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 11
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 11:
            self.cls_m.type = BELT
            self.cls_m.orientation = orientations[3]
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 12
        elif keys[pygame.K_x] and board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] == 12:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 9
        elif keys[pygame.K_z]:
            board.board[self.m_pos_y // board.cl_size][self.m_pos_x // board.cl_size] = 0
            self.cls_m.type = None
        elif self.cls_m.type == DRILLER:
            for i in range(MachineLib.lib[DRILLER]['opTime']):
                if i == MachineLib.lib[DRILLER]['opTime'] and (
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 23 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 24 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 25 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 26):
                    ClsMaterial.type = 'Red'
                    self.contains += ClsMaterial.type
                if i == MachineLib.lib[DRILLER]['opTime'] and (
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 27 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 28 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 29 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 30):
                    ClsMaterial.type = 'Green'
                    self.contains += ClsMaterial.type
                if i == MachineLib.lib[DRILLER]['opTime'] and (
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 31 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 32 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 33 or
                        board.board[player.m_pos_y // board.cl_w][player.m_pos_x // board.cl_w] == 34):
                    ClsMaterial.type = 'Blue'
                    self.contains += ClsMaterial.type
                    print(self.contains)

# --------Материалы-------- #


class ClsMaterial:
    def __init__(self, main, material, x, y, orientation, quantity):
        self.main = main
        self.type = material
        self.x = x
        self.y = y
        self.orientation = orientation
        self.quantity = quantity
        self.cost = self.main.MaterialLib.lib[self.type]['cost']


MachineLib = MachineLib()
board = Board()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #player.inter(ClsMachine)
    player.inter(board)
    win.fill((100, 100, 100))
    board.render()
    clock.tick(FPS)
    pygame.display.update()



