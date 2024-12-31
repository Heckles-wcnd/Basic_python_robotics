from robot_control_class import RobotControl
import math

class RunLaser:
    def __init__(self, speed, dist):
        self.rc = RobotControl()
        self.speed = speed
        self.dist = dist

    def get_full_laser(self):
        """Get all laser distances as a list."""
        return self.rc.get_laser_full()

    def rotate_to_max_distance(self, laser_data):
        """Rotate to the direction of the maximum laser distance, handling 'inf' values."""
        if not laser_data:  # Check if laser_data is empty
            print("Error: Laser data is empty!")
            return

        print("Original Laser Data:", laser_data)

        # Replace 'inf' values with a large number for comparison
        cleaned_data = [round(self.dist + 10, 2) if x == float('inf') else round(x, 2) for x in laser_data]
        
        print("Cleaned Data:", cleaned_data)

        if not cleaned_data:
            print("Error: Cleaned data is empty!")
            return
        
        max_distance = max(cleaned_data)

        print("Max Distance:", max_distance)

        # Find all indices with the maximum distance
        max_indices = [i for i, d in enumerate(cleaned_data) if d == max_distance]

        print("Max Indices:", max_indices)

        if not max_indices:
            print("Error: No valid maximum distance found!")
            

        # Calculate the median index
        max_index = int(sorted(max_indices)[len(max_indices) // 2])

        print("Selected Max Index:", max_index)

        # Calculate angle to rotate (0 index corresponds to -90 degrees, 719 to +90 degrees)
        angle = (max_index - 360) * 0.25

        print("Rotation Angle:", angle)

        # Rotate to face the direction of max distance
        self.rc.rotate(angle)

    def move_straight(self):
        """Continuously move the robot straight at the specified speed."""
        self.rc.cmd.linear.x = self.speed  # set speed
        self.rc.cmd.angular.z = 0.0        # no rotation
        self.rc.publish_once_in_cmd_vel()  # continue to move straight

    def stop(self):
        """Stop the robot."""
        self.rc.stop_robot()

    def run(self):
        """Main loop for continuous movement and distance checking."""
        while True:
            self.move_straight()  # Continuously move straight

            # Get the full laser data
            laser_data = self.get_full_laser()

            # Focus on the front region 
            front_distances = laser_data[300:420]
            front_distances = [d if d != float('inf') else self.dist + 1 for d in front_distances]  # Handle 'inf'

            # Calculate the average and minimum distances in the front region
            average_distance = sum(front_distances) / len(front_distances)
            min_distance = min(front_distances)

            # Count the number of points below the safety threshold
            below_threshold = sum(1 for d in front_distances if d < self.dist)
            below_threshold_ratio = below_threshold / len(front_distances)

            # Log the computed values
            print(f"Average Distance: {average_distance:.2f}, Min Distance: {min_distance:.2f}, Below Threshold Ratio: {below_threshold_ratio:.2f}")

            # Determine if there's an obstacle based on multiple conditions
            if min_distance < self.dist or below_threshold_ratio > 0.5:
                # Stop and determine the next direction
                self.stop()
                self.rotate_to_max_distance(laser_data)


if __name__ == '__main__':
    navigator = RunLaser(speed=0.4, dist=0.9)
    navigator.run()