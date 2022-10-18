import pygame

# initialization
pygame.init()
clock = pygame.time.Clock()

# set up surface
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# text strings
base_font = pygame.font.Font(None, 32)
user_text = '>'
display_text = 'Text description of room'
title_text = 'Dungeon'
map_text = 'Connected Rooms'
inventory_text = 'Inventory'
test_nav_text_1 = 'N: Dungeon Cell 1'
test_nav_text_2 = 'E: Dungeon Cell 2'
test_nav_text_3 = 'W: Dungeon Cell 3'

help_text_1 = '/help'
help_text_2 = '/move'
help_text_3 = '/look'

map_help = 'Click on a location to move there'
inventory_help = 'Click an item for more information'
first_start_help_text = 'Enter text at the > prompt or'
first_start_help_2_text = 'click the navigation icons under Connected Rooms!'

# rectangles for blocking off UI areas
help_rect = pygame.Rect(screen_width * 0.6 - 100, screen_height - 100, 100, 100)                    # help text rectangle
title_rect = pygame.Rect(0, 0, screen_width * 0.6, screen_height * 0.1)                             # room title rectangle
inventory_rect = pygame.Rect(screen_width * 0.6, 10, screen_width * 0.4 - 10, 225)                  # inventory rectangle
map_rect = pygame.Rect(screen_width * 0.6, 250, screen_width * 0.4 - 10, 250)                       # map rectangle
input_rect = pygame.Rect(screen_width * 0.6, screen_height - 32 - 5, screen_width * 0.4 - 10, 32)   # input rectangle
output_rect = pygame.Rect(screen_width * 0.6, screen_height * 0.7 + 10, screen_width * 0.4 - 10,    # output rectangle
                          screen_height - (screen_height * 0.7) - 50)

map_desc_rect = pygame.Rect(screen_width * 0.6 + 5, 250 + 5, screen_width * 0.4 - 10, 32)
nav_text_1_rect = pygame.Rect(screen_width * 0.6, 255 + 32, screen_width * 0.4 - 10, 32)
nav_text_2_rect = pygame.Rect(screen_width * 0.6, 255 + 64, screen_width * 0.4 - 10, 32)
nav_text_3_rect = pygame.Rect(screen_width * 0.6, 255 + 96, screen_width * 0.4 - 10, 32)

inv_desc_rect = pygame.Rect(screen_width * 0.6 + 5, 15, screen_width * 0.4 - 10, 32)

# colors
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
output_color = pygame.Color('red')
map_color = pygame.Color('blue')
inventory_color = pygame.Color('green')

# flags for drawing/highlighting
active = False
draw_help_box = False
draw_map_help = False
draw_inventory_help = False
first_start_help = True

# image path
path_to_image = 'images/dungeon.jpeg'

# image width and height
width = screen_width
height = screen_height

# event loop
while True:
    # process player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            elif first_start_help:
                first_start_help = False
            elif nav_text_1_rect.collidepoint(event.pos):
                user_text = test_nav_text_1
            elif nav_text_2_rect.collidepoint(event.pos):
                user_text = test_nav_text_2
            elif nav_text_3_rect.collidepoint(event.pos):
                user_text = test_nav_text_3
            elif map_desc_rect.collidepoint(event.pos):
                draw_map_help = True
            elif inventory_rect.collidepoint(event.pos):
                draw_inventory_help = True
            else:
                draw_map_help = False
                draw_inventory_help = False
                active = False

        # keyboard input
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    draw_help_box = False
                    user_text = user_text[:-1]
                elif event.key == pygame.K_SLASH and len(user_text) <= 1:
                    draw_help_box = True
                    user_text += event.unicode
                elif event.key == pygame.K_RETURN:
                    draw_help_box = False
                    display_text = f"You entered: {user_text[1:]}"
                    user_text = '>'
                else:
                    draw_help_box = False
                    user_text += event.unicode

    # fill screen with background color
    screen.fill((0, 0, 0))

    # draw the room title
    title_text_surface = base_font.render(title_text, True, (255, 255, 255))
    screen.blit(title_text_surface, (title_rect.x, title_rect.y))

    # draw the room image
    image = pygame.transform.scale(pygame.image.load(path_to_image), [int(width) * 0.6, int(height) * 0.9])
    screen.blit(image, (0,height * 0.1))

    # draw the help box
    if draw_help_box:
        pygame.draw.rect(screen, map_color, help_rect, 2)
        help_text_surface = base_font.render(help_text_1, True, (255, 255, 255))
        screen.blit(help_text_surface, (help_rect.x + 5, help_rect.y + 5))

    # draw the map box and text
    pygame.draw.rect(screen, map_color, map_rect, 2)
    map_text_surface = base_font.render(map_text, True, (255, 255, 255))
    screen.blit(map_text_surface, (map_desc_rect.x, map_desc_rect.y))

    nav_text_1_surface = base_font.render(test_nav_text_1, True, (255, 255, 255))
    screen.blit(nav_text_1_surface, (nav_text_1_rect.x + 5, nav_text_1_rect.y + 5))

    nav_text_2_surface = base_font.render(test_nav_text_2, True, (255, 255, 255))
    screen.blit(nav_text_2_surface, (nav_text_2_rect.x + 5, nav_text_2_rect.y + 5))

    nav_text_3_surface = base_font.render(test_nav_text_3, True, (255, 255, 255))
    screen.blit(nav_text_3_surface, (nav_text_3_rect.x + 5, nav_text_3_rect.y + 5))

    # draw the inventory box and text
    pygame.draw.rect(screen, inventory_color, inventory_rect, 2)
    inventory_text_surface = base_font.render(inventory_text, True, (255, 255, 255))
    screen.blit(inventory_text_surface, (inv_desc_rect.x, inv_desc_rect.y))

    # draw the help boxes
    if draw_inventory_help:
        inv_help_surface = base_font.render(inventory_help, True, (255, 255, 255))
        screen.blit(inv_help_surface, (inventory_rect.x - inv_help_surface.get_width(), inventory_rect.y))
    if draw_map_help:
        map_help_surface = base_font.render(map_help, True, (255,255,255))
        screen.blit(map_help_surface, (map_rect.x - map_help_surface.get_width(), map_rect.y))

    if first_start_help:
        first_start_surface_1 = base_font.render(first_start_help_text, True, (255,255,255))
        screen.blit(first_start_surface_1, (50, screen_height / 2))
        first_start_surface_2 = base_font.render(first_start_help_2_text, True, (255, 255, 255))
        screen.blit(first_start_surface_2, (50, screen_height / 2 + 32))

    # determine the color of the input text box
    if active:
        color = color_active
    else:
        color = color_passive

    # draw the input text box
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # draw the output text box
    pygame.draw.rect(screen, output_color, output_rect, 2)
    output_text_surface = base_font.render(display_text, True, (255,255,255))
    screen.blit(output_text_surface, (output_rect.x + 5, output_rect.y + 5))

    # update the screen
    pygame.display.flip()
    clock.tick(60)
