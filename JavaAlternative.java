import java.util.Scanner;

public class BallTrajectory {
    private static final double GRAVITY = 9.81;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter initial velocity (m/s): ");
        double velocity = scanner.nextDouble();

        System.out.print("Enter launch angle (degrees): ");
        double angle = Math.toRadians(scanner.nextDouble());

        double timeOfFlight = (2 * velocity * Math.sin(angle)) / GRAVITY;
        double maxHeight = (Math.pow(velocity, 2) * Math.pow(Math.sin(angle), 2)) / (2 * GRAVITY);
        double range = (Math.pow(velocity, 2) * Math.sin(2 * angle)) / GRAVITY;

        System.out.printf("Max Height: %.2f meters\n", maxHeight);
        System.out.printf("Range: %.2f meters\n", range);

        scanner.close();
    }
}
