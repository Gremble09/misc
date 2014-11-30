#include <iostream>

void ToH(int DiskToMove, char fromStack, char toStack, char otherStack)
{
    if ( DiskToMove != 0)
    {
        ToH(DiskToMove-1, fromStack, otherStack, toStack);
        std:: cout << fromStack << " -> " << toStack << "\n";
        ToH(DiskToMove-1, otherStack, toStack, fromStack);
    }
}

int main()
{
    std:: cout << "Let's play a game.\n";
    std:: cout << "Tower of Hanoi for n = ";
    int input;
    std:: cin >> input;
    ToH(input, 'A', 'B', 'C');
    return 0;
}

