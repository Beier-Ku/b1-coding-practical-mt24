from uuv_mission.mission import Mission

# Use full path to find mission.csv
mission = Mission.from_csv("C:/Users/admin/Desktop/Engineering/B1-coding practical/b1-coding-practical-mt24-main/data/mission.csv")
print(mission.data)

# Test the updated methods
print("Mission Reference Range:", mission.get_mission_reference_range())
print("Max Cave Height:", mission.get_max_cave_height(), "meters")
print("Min Cave Height:", mission.get_min_cave_height(), "meters")
print("Max Cave Depth:", mission.get_max_cave_depth(), "meters")
print("Min Cave Depth:", mission.get_min_cave_depth(), "meters")
print("Average Cave Height Change:", mission.get_average_cave_height_change(), "meters")
print("Average Cave Depth Change:", mission.get_average_cave_depth_change(), "meters")