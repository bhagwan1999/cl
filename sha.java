import java.math.BigInteger; 
import java.security.MessageDigest; 
import java.security.NoSuchAlgorithmException; 
import java.util.Scanner;

public class sha { 
	public static String encryptThisString(String input) 
	{ 
		try { 
			// getInstance() method is called with algorithm SHA-1 
			MessageDigest md = MessageDigest.getInstance("SHA-1"); 

			// digest() method is called 
			// to calculate message digest of the input string 
			// returned as array of byte 
			byte[] messageDigest = md.digest(input.getBytes()); 

			// Convert byte array into signum representation 
			BigInteger no = new BigInteger(1, messageDigest); 

			// Convert message digest into hex value 
			String hashtext = no.toString(16); 

			// Add preceding 0s to make it 32 bit 
			while (hashtext.length() < 32) { 
				hashtext = "0" + hashtext; 
			} 

			// return the HashText 
			return hashtext; 
		} 

		// For specifying wrong message digest algorithms 
		catch (NoSuchAlgorithmException e) { 
			throw new RuntimeException(e); 
		} 
	} 

	// Driver code 
	public static void main(String args[]) throws NoSuchAlgorithmException 
	{ 

		Scanner in = new Scanner(System.in);

		System.out.println("Enter String: "); 

		String s1 = in.nextLine();
		System.out.println("\n" + s1 + " : " + encryptThisString(s1)); 

	} 
} 
