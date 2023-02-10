import sys

from geocoder import *
from mapapi_PG import *


def main():
    toponym = 'Кириши Ленинградская 6'

    if not toponym:
        print('No data')
    else:
        ll, spn = get_ll_span(toponym)
        ll_spn = f"ll={ll}"
        point = f'pt={ll},pm2wtl'

        z = 10

        map_file = show_map(ll_spn, "map", add_params=f'&z={z}')

        running = True
        pygame.init()
        screen = pygame.display.set_mode((600, 450))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
        os.remove(map_file)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                key = pygame.key.get_pressed()

                if z < 23:
                    if key[pygame.K_UP]:
                        z += 1
                        map_file = show_map(ll_spn, "map", add_params=f'&z={z}')
                        screen.blit(pygame.image.load(map_file), (0, 0))
                        pygame.display.flip()
                        os.remove(map_file)
                if z > 0:
                    if key[pygame.K_DOWN]:
                        z -= 1
                        map_file = show_map(ll_spn, "map", add_params=f'&z={z}')
                        screen.blit(pygame.image.load(map_file), (0, 0))
                        pygame.display.flip()
                        os.remove(map_file)
            pygame.display.flip()


if __name__ == '__main__':
    main()