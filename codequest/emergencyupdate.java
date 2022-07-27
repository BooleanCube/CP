import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class emergencyupdate {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        for(int k=0; k<t; k++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int o = Integer.parseInt(st.nextToken()), n = Integer.parseInt(st.nextToken());
            ArrayList<String> output = new ArrayList<>();
            ArrayList<Contact> original = new ArrayList<>();
            for(int i=0; i<o; i++) {
                String[] line = bf.readLine().split(",");
                Contact c = new Contact(line[0], Long.parseLong(line[1]), line[2]);
                original.add(c);
            }
            ArrayList<Contact> newc = new ArrayList<>();
            for(int i=0; i<n; i++) {
                String[] line = bf.readLine().split(",");
                Contact c = new Contact(line[0], Long.parseLong(line[1]), line[2]);
                newc.add(c);
                boolean match = true;
                for(Contact co : original)
                    if(co.name.equals(c.name)) {
                        match = false;
                        if(co.phone != c.phone && !co.address.equals(c.address)) output.add(c.name + " UPDATED BOTH");
                        else if(co.phone != c.phone) output.add(c.name + " UPDATED PHONE NUMBER");
                        else if(!co.address.equals(c.address)) output.add(c.name + " UPDATED ADDRESS");
                    }
                if(match) output.add(c.name + " CREATED");
            }
            for(Contact f : original) {
                boolean match = true;
                for(Contact s : newc) {
                    if(s.name.equals(f.name)) {
                        match = false;
                        break;
                    }
                }
                if(match) output.add(f.name + " DELETED");
            }
            Collections.sort(output);
            System.out.println(String.join("\n", output));
        }
    }

}

class Contact {
    public String name;
    public long phone;
    public String address;
    public Contact(String n, long p, String a) {
        name = n; phone = p; address = a;
    }
    public boolean equals(Contact c) {
        return name.equals(c.name) && phone == c.phone && address.equals(c.address);
    }
}
