import javax.swing.*;
import java.text.DecimalFormat;

/**
 * Codecademy project - TransitCalculator
 * @author - Slava Tashlyk
 * @version - 20.10.2022
 */
public class TransitCalculator
{

	private int numDays;
	private int numRides;

	public final double PAY_PER_RIDE = 2.75;
	public final double SEVEN_DAY_UNLIMITED = 33.00;
	public final double THIRY_DAY_UNLIMITED = 127.00;

	/**
	 * TransitCalculator constructor.
	 * @param numDaysIn - number of days.
	 * @param numRidesIn - number of rides.
	 */
	public TransitCalculator(int numDaysIn, int numRidesIn)
	{
		numDays = numDaysIn;
		numRides = numRidesIn;
	}

	/**
	 * Method that get the price per ride if purchasing 7-day pass.
	 * @return - the overall price per ride of using the 7-day Unlimited option.
	 */
	public double unlimited7Price()
	{
		double pricePerRide = 0;
		int totalPasses = (numDays / 7) + 1:
		double totalPrice = totalPasses * SEVEN_DAY_UNLIMITED;
		pricePerRide = totalPrice / numRides;
		return pricePerRide;
	}

	/**
	 * Method that calculate the price per ride for each fare option
	 * @return - an array of the price per ride for the three fare options.
	 */
	public double[] getRidePrices()
	{
		double[] prices = new double[3];
		prices[0] = PAY_PER_RIDE;
		prices[1] = this.unlimited7Price();
		prices[2] = THIRY_DAY_UNLIMITED / numRides;
		return prices;
	}

	/**
	 * Method that the best fare given #of rides and #of days
	 * @return - String that communicates the findings.
	 */
	public String getBestFare()
	{
        DecimalFormat df = new DecimalFormat("$#0.00");
        String advice = "You should get the ";
        double[] prices = this.getRidePrices();

        if(prices[0] <= prices[1] && prices[0] <= prices[2]) 
        {
            advice += "Pay-per-ride option at " + df.format(PAY_PER_RIDE) + " per ride.";
        } 
        else if (prices[1] <= prices[2]) 
        {
            advice += "7-day Unlimited option at " + df.format(prices[1]) + " per ride.";
        }
        else if (prices[2] <= prices[1] && prices[2] <= prices[0]) 
        {
            advice += "30-day Unlimited option at " + df.format(prices[2]) + " per ride.";
        } 
        else 
        {
            advice += "heck out of dodge! Just kidding my program is broken lulz.";
        }
        return advice;		
	}

	public int getNumDays() 
	{
        return numDays;
    }

    public void setNumDays(int numDays) 
    {
        this.numDays = numDays;
    }

    public int getNumRides() 
    {
        return numRides;
    }

    public void setNumRides(int numRides) 
    {
        this.numRides = numRides;
    }

    public static void main(String[] args) {
        String input = null;
        int numDays;
        int numRides;
        int runAgain = 0;

        do 
        { 
            try 
            {
                input = (JOptionPane.showInputDialog("How many days will you be riding?"));
                if (input == null) {return;} 
                numDays = Integer.parseInt(input);

                input = (JOptionPane.showInputDialog("How many rides?"));
                if (input == null) {return;} 
                numRides = Integer.parseInt(input);

                TransitCalc yourRecommendation = new TransitCalc(numDays, numRides);
                JOptionPane.showMessageDialog(null, yourRecommendation.getBestFare());

                runAgain = JOptionPane.showConfirmDialog(null, "Calculate again?"); 
            } 
            catch (NumberFormatException e) 
            {
                JOptionPane.showMessageDialog(null, "Please enter a positive integer.");
            }
        } 
        while ((runAgain == 0));
    }    
}