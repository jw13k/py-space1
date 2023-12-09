# 사용자로부터 도보 속도 입력 받기 (킬로미터/시간)
flat_terrain_speed = float(input("평지에서의 도보 속도를 입력하세요 (킬로미터/시간): "))
forest_speed = float(input("숲에서의 도보 속도를 입력하세요 (킬로미터/시간): "))
river_speed = float(input("강을 건너는 도보 속도를 입력하세요 (킬로미터/시간): "))
mountain_speed = float(input("산을 오르는 도보 속도를 입력하세요 (킬로미터/시간): "))
cliff_speed = float(input("절벽을 오르는 도보 속도를 입력하세요 (킬로미터/시간): "))

# 사용자로부터 각 지형을 거치는 시간 입력 받기 (시간)
forest_time = float(input("숲을 거치는 시간을 입력하세요 (시간): "))
river_time = float(input("강을 건너는 시간을 입력하세요 (시간): "))
mountain_time = float(input("산을 오르는 시간을 입력하세요 (시간): "))
cliff_time = float(input("절벽을 오르는 시간을 입력하세요 (시간): "))

# 각 지형을 거치는 동안 이동한 거리 계산
forest_distance = forest_speed * forest_time
river_distance = river_speed * river_time
mountain_distance = mountain_speed * mountain_time
cliff_distance = cliff_speed * cliff_time

# 총 이동 거리 계산
total_distance = forest_distance + river_distance + mountain_distance + cliff_distance

# 결과 출력
print("숲을 거치는 동안 이동한 거리: {:.2f} 킬로미터".format(forest_distance))
print("강을 건너는 동안 이동한 거리: {:.2f} 킬로미터".format(river_distance))
print("산을 오르는 동안 이동한 거리: {:.2f} 킬로미터".format(mountain_distance))
print("절벽을 오르는 동안 이동한 거리: {:.2f} 킬로미터".format(cliff_distance))
print("총 이동 거리: {:.2f} 킬로미터".format(total_distance))
