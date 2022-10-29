public class Droid
{
  int batteryLevel;
  String name;

  public Droid(String droidName)
  {
    name = droidName;
    batteryLevel = 100;
  }
  
  public String toString()
  {
    return "Hello, I'm the droid: " + name;
  }

  public void performTask(String task)
  {
    System.out.println("[#] " + name + " is performing task: " + task);
    batteryLevel -= 10;
  }

  public String energyReport()
  {
    return "[!] Battery level report:\n" + "    > "+ name + " - " + batteryLevel + "%";
  }

  public void energyTransfer(Droid sourceDroidObject, int transferedEnergy)
  {
    this.batteryLevel += transferedEnergy;
    sourceDroidObject.batteryLevel -= transferedEnergy;
    System.out.println("[#] " + sourceDroidObject.name + " transfered " + transferedEnergy + " energy to " + this.name);
  }
  
  public static void main(String[] args)
  {
    Droid Codey = new Droid("Codey");
    Codey.performTask("Dancing");
    Codey.performTask("Levitating");
    System.out.println(Codey.energyReport());

    Droid Margot = new Droid("Margot");
    Margot.performTask("Dancing");
    Margot.performTask("Reading");
    Margot.performTask("Coocking");
    Margot.performTask("Runing");
    Margot.performTask("Study Java");
    System.out.println(Margot.energyReport());

    Codey.energyTransfer(Margot, 10);
    System.out.println(Codey.energyReport());
    System.out.println(Margot.energyReport());    
  }
}