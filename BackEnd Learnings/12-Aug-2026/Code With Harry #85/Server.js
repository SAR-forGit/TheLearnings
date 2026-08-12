var slugify = require('slugify')

a = slugify('some string') // some-string
console.log(a);


// if you prefer something other than '-' as separator
b = slugify('some string&&**/*/--', '_')  // some_string
console.log(b);