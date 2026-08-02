function  adjectives (random = Math.random()){
    a = "crazy", b = 'amazing', c = "fire";
    console.log(random);
    if (random < 1 && random > 0.66) return a;
    else if (random < 0.66 && random > 0.33 ) return b;
    else return c;
}

function shop_name(random = Math.random()){
    a = "engine", b = 'food', c = "garments";
    console.log(random);
    if (random < 1 && random > 0.66) return a;
    else if (random < 0.66 && random > 0.33 ) return b;
    else return c;
}

function another_word(random = Math.random()){
    a = "bros", b = 'limited', c = "hub";
    console.log(random);
    if (random < 1 && random > 0.66) return a;
    else if (random < 0.66 && random > 0.33 ) return b;
    else return c;
}

adjectives = adjectives();
shop_name = shop_name();
another_word = another_word();

console.log(`Your random bussiness name is ${adjectives} ${shop_name} ${another_word}`)