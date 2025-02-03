# include <stdio.h>

void Asalamualaykum ();
void hello ();
void bonjour ();
void Indian ();

int main () {
    
    char nationality;
    printf ("Enter your nationality: \n\n");
    
    printf ("(S for Saudi, F for French, I for Indian & A for American): ");
    scanf ("%c", &nationality);
    
    if (nationality == 'S') {
        Asalamualaykum();
    } 
    else if (nationality == 'F') {
        bonjour ();
    }
    else if (nationality == 'I') {
        Indian ();
        
    }
    
else {
    hello ();
    
}

return 0;

}


void Indian () {
    printf ("Aur Kaise hain aap?");
}

void Asalamualaykum () {
    printf ("Asalamu Alaykum Habibi \n");
    
}
void hello () {
    printf ("Hello there \n");
}
void bonjour () {
    
    printf ("Bonjour amie \n");
    
}
 