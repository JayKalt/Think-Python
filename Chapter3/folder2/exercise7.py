# Enhance your program above to also tell us what the drunk pirate’s heading is after he has finished stumbling
# around. (Assume he begins at heading 0).

experimental_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
final_heading = 0

for angle in experimental_data:
	final_heading += angle

print("Pirate's heading after he has finished stumbling around is", final_heading % 360)
