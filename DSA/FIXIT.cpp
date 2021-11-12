#include <deque>
#include <iostream>
#include <ctype.h>
using namespace std;

class stack {
  public:
    deque<char>* s = new deque<char>();
    int size() { return s->size(); }
    void push(char c) { s->push_back(c); }
    char peek() { return s->back(); }
    string toString() { 
      string a; 
      for(char c : *s) { a.push_back(c); a+=" "; } 
      return a;
    }
    char pop() { char c = peek(); s->pop_back(); return c; }
};

int pemdas(char op) {
  if(op == '+' || op == '-') return 1;
  if(op == '*' || op == '/') return 2;
  if(op == '^') return 3;
  return -1;
}

int main() {
  stack* s = new stack();
  while(true) {
    string inp; cin >> inp;
    string out;
    for(int i=0; i<inp.length(); i++) {
      char c = inp.at(i);
      if(isalpha(c) || isdigit(c)) { out.push_back(c); out.push_back(' '); }
      else if(c == '(') s->push(c);
      else if(c == ')') {
        while(s->size() > 0 && s->peek() != '(') { out.push_back(s->pop()); out.push_back(' '); }
        s->pop();
      }
      else {
        while(s->size() > 0 && pemdas(c) <= pemdas(s->peek())) { out.push_back(s->pop()); out.push_back(' '); }
        s->push(c);
      }
    }
    while(s->size() > 0) { out.push_back(s->pop()); out.push_back(' '); }
    cout << out << endl;
  }
  return 0;
}
