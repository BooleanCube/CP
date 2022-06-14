import java.io.*;
import java.util.*;

public class GeneralToBST {
    public static void main(String[] args) throws IOException {
        
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        
        //Constructing General Tree
        Node head = new Node("A", new ArrayList<Node>());
        Tree general = new Tree(head);
        head.children.add(new Node("B", new ArrayList<Node>()));
        head.children.add(new Node("C", new ArrayList<Node>()));
        head.children.get(0).children.add(new Node("D", new ArrayList<Node>()));
        head.children.get(0).children.add(new Node("E", new ArrayList<Node>()));
        head.children.get(1).children.add(new Node("F", new ArrayList<Node>()));
        head.children.get(1).children.add(new Node("G", new ArrayList<Node>()));
            head.children.get(1).children.add(new Node("H", new ArrayList<Node>()));
        
            //Displaying the General Tree
            System.out.println(general.toString());

            //Converting the General Tree into a Binary Tree
            Tree BST = general.convertToBST();

            //Displaying the Binary Tree
            System.out.println(BST.toString());
        
    }
}

class Tree {
    
    public Node head;
    
    public Tree(Node head) {
        this.head = head;
    }

    public Tree() {}
    
    public Tree convertToBST() {
        ArrayDeque<Node> q = new ArrayDeque<Node>();
        q.addLast(head);
        Tree bst = new Tree();
        bst.head = new Node(head.name, new ArrayList<Node>());
        Node BSTCurrent = bst.head;
        while(!q.isEmpty()) {
            Node current = q.removeFirst();
            if(current.children.isEmpty()) continue;
            Node BSTEquiv = findBSTNode(bst, current.name);
            if(BSTEquiv != null) BSTCurrent = BSTEquiv;
            BSTCurrent.children.add(0, new Node(current.children.get(0).name, new ArrayList<Node>()));
            BSTCurrent = BSTCurrent.children.get(0);
            q.addLast(current.children.get(0));
            Node org = BSTCurrent;
            for(int i=1; i<current.children.size(); i++) {
                q.addLast(current.children.get(i));
                BSTCurrent.children.add(new Node(current.children.get(i).name, new ArrayList<Node>()));
                BSTCurrent = BSTCurrent.children.get(0);
            }
            BSTCurrent = org;
        }
        return bst;
    }

        public Node findBSTNode(Tree bst, String name) {
        ArrayDeque<Node> q = new ArrayDeque<Node>();
        q.add(bst.head);
        while(!q.isEmpty()) {
            Node current = q.removeFirst();
            if(current.name.equals(name)) return current;
            for(Node n : current.children) q.add(n);
        }
        return null;
        }

        public String toString() {
        StringBuilder sb = new StringBuilder();
        ArrayDeque<Node> q = new ArrayDeque<Node>();
        q.add(head);
        sb.append("0-").append(head.name).append("\n");
        while(!q.isEmpty()) {
            int numOfChld = q.size();
            for(int i=0; i<numOfChld; i++) {
            Node current = q.removeFirst();
            for(Node n : current.children) {
                q.add(n);
                sb.append(current.name).append("-").append(n.name).append(" ");
            }
            sb.append(" ");
            }
            sb.append("\n");
        }
        return sb.toString();
        }
    
}

class Node {
    
    public String name;
    public ArrayList<Node> children;
    
    public Node(String name, ArrayList<Node> children) {
        this.name = name;
        this.children = children;
    }
    
}
