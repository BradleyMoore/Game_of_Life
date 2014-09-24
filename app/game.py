TO_LIVE = [2, 3]
TO_BE_BORN = [3]


def draw_game():
    pass


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def game_actions():
	pass
