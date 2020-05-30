import pygame

from Console import Message, Console

# list of legal keys we can type into console
legal_console_keys = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
                      pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p,
                      pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
                      pygame.K_y, pygame.K_z]

user_input = ""

# determines if we are typing in a 'say' string...
COMMAND_MODE = 0
SAY_MODE = 1

# initialize a console
console = Console(10)

class Handler:

    def __init__(self):
        self.user_input = ">"
        self.console_mode = COMMAND_MODE
        self.console = console

        self._selecting = False

    def handle(self,event, npc, canvas):
        if event.type == pygame.QUIT:
            crashed = True

        if self._selecting:
            x, y = pygame.mouse.get_pos()

            canvas.drawSelectionBox(x,y)

            if event.type == pygame.MOUSEBUTTONUP:
                console.push("mouse button released")
                self._selecting = False
                canvas.endDrawSelection()

                # get selected targets

        if event.type == pygame.MOUSEBUTTONDOWN:
            console.push("mouse button down")
            # Set the x, y postions of the mouse click
            x, y = event.pos

            if npc.collided(x, y):
                # custom message with images
                # color sprite
                colorimage = pygame.surfarray.array3d(npc.sprite)
                colorimage = colorimage[1, :, :]
                out = pygame.surfarray.make_surface(colorimage)
                message = Message(["selected", npc.name, "selected", npc.name], [npc.sprite, npc.sprite])
                console.push(message)

            else:
                canvas.startDrawSelection(x,y)
                self._selecting = True


        # say move
        if self.console_mode == SAY_MODE:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[0:5] + self.user_input[5:len(self.user_input) - 3] + " \""
                    if len(self.user_input) == 7:
                        self.mode = COMMAND_MODE
                        self.user_input = ">"
                elif event.key == pygame.K_RETURN:
                    self.mode = COMMAND_MODE
                elif event.key == pygame.K_SPACE:
                    self.user_input = self.user_input[:len(self.user_input) - 2] + "  \""
                elif event.key in legal_console_keys:
                    key = pygame.key.name(event.key)
                    self.user_input = self.user_input[:len(self.user_input) - 2] + key + " \""

        if self.console_mode == COMMAND_MODE:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_UP:
                    y_change = -1
                elif event.key == pygame.K_DOWN:
                    y_change = 1
                key = pygame.key.name(event.key)
                # console input
                if event.key == pygame.K_SPACE:
                    self.user_input += " "
                elif event.key == pygame.K_BACKSPACE:
                    if self.user_input != ">":
                        self.user_input = self.user_input [:len(self.user_input ) - 1]
                elif event.key == pygame.K_RETURN:

                    console.push(self.user_input [1:])
                    self.user_input = ">"
                # if it wasn't a movement't option it was textual input for the console
                elif event.key in legal_console_keys:

                    if self.console_mode == COMMAND_MODE:
                        self.user_input += key.upper()

                        if self.user_input == ">SAY":
                            self.console_mode = SAY_MODE
                            self.user_input = ">SAY \"  \""

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0