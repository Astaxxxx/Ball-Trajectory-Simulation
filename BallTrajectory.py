import math
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)

# Function to calculate the ball's trajectory
def calculate_trajectory(velocity, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    # Time of flight
    time_of_flight = (2 * velocity * math.sin(angle_radians)) / GRAVITY

    # Max height
    max_height = (velocity**2 * math.sin(angle_radians)**2) / (2 * GRAVITY)

    # Horizontal range
    range_distance = (velocity**2 * math.sin(2 * angle_radians)) / GRAVITY

    # Time intervals for simulation
    time_intervals = [i * 0.01 for i in range(int(time_of_flight / 0.01) + 1)]
    
    x_positions = []
    y_positions = []
    
    for t in time_intervals:
        # Calculate position at time t
        x = velocity * t * math.cos(angle_radians)
        y = (velocity * t * math.sin(angle_radians)) - (0.5 * GRAVITY * t**2)
        
        x_positions.append(x)
        y_positions.append(y)
    
    return x_positions, y_positions, max_height, range_distance

# Function to plot the trajectory
def plot_trajectory(x_positions, y_positions, velocity, angle):
    plt.plot(x_positions, y_positions, label=f"v={velocity} m/s, θ={angle}°")
    plt.title("Ball Trajectory Simulation")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
if __name__ == "__main__":
    # Input values
    velocity = float(input("Enter initial velocity of the ball (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))

    # Calculate trajectory
    x_positions, y_positions, max_height, range_distance = calculate_trajectory(velocity, angle)

    # Display results
    print(f"Max Height: {max_height:.2f} meters")
    print(f"Range: {range_distance:.2f} meters")

    # Plot the trajectory
    plot_trajectory(x_positions, y_positions, velocity, angle)
