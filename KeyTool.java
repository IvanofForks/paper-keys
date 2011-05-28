
import com.google.bitcoin.core.*;


public class KeyTool {
    
    public static void main(String args[]) {
        
        if (args[0].equals("--gen-keys")) {
            int n = Integer.parseInt(args[1]);
            System.out.println("{\"keys\":[");
            for (int i = 0; i < n; i++) {
                if (i > 0) {
                    System.out.println(",");
                }
                System.out.println("{");
                
                ECKey key = new ECKey();
                String priv58 = Base58.encode(key.getPrivKey().toByteArray());
                String address = key.toAddress(NetworkParameters.prodNet()).toString();
                
                System.out.println("\"priv58\": \"" + priv58 + "\",");
                System.out.println("\"address\": \"" + address.toString() + "\"");
                
                System.out.println("}");
            }
            System.out.println("]}");
        }
    }
}
