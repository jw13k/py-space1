import pygame
import sys
import random
import simpleaudio

# Pygame 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainy Day")

# 배경 음악 설정
bg_music = pygame.mixer.Sound("background_music.wav")  # 배경 음악 파일을 background_music.wav로 바꿔주세요
pygame.mixer.music.set_volume(0.5)

# 배경 설정
background_color = (0, 0, 0)  # 검은색 배경

# 비 드롭 설정
raindrop_image = pygame.image.load("raindrop.png")  # 비 이미지 파일을 raindrop.png로 바꿔주세요
raindrop_speed = 5
raindrops = []

# 마우스 빈도, 비 크기, 배경 음악 설정
mouse_frequency = 0.1
raindrop_size = 1.0
music_playing = False

# 시계 설정
clock = pygame.time.Clock()

# 이벤트 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 마우스 이벤트 처리
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            mouse_frequency = (mouse_x / width) * 0.5  # 마우스 X 위치에 따라 빈도 동적 조절

        # 마우스 휠 이벤트 처리
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            raindrop_size += 0.1  # 마우스 휠을 위로 스크롤하면 비 크기 증가
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            raindrop_size = max(0.1, raindrop_size - 0.1)  # 마우스 휠을 아래로 스크롤하면 비 크기 감소

        # 키보드 이벤트 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.Sound.play(bg_music, loops=-1)
                music_playing = not music_playing

    # 비 생성
    if random.random() < mouse_frequency:
        x = random.randint(0, width)
        y = 0
        raindrops.append([x, y])

    # 비 이동
    for drop in raindrops:
        drop[1] += raindrop_speed

    # 비 크기 조절
    raindrop_scaled = pygame.transform.scale(raindrop_image, (int(20 * raindrop_size), int(20 * raindrop_size)))

    # 비 화면 밖으로 나가면 삭제
    raindrops = [drop for drop in raindrops if drop[1] < height]

    # 화면 초기화
    screen.fill(background_color)

    # 비 그리기
    for drop in raindrops:
        screen.blit(raindrop_scaled, (drop[0], drop[1]))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    clock.tick(60)
