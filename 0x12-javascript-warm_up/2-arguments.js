#!/usr/bin/node

// process.argv property is an inbuilt application
// Return Value: This property returns an array
// containing the arguments passed to the process
// when run it in the command line. The first
// element is the process execution path and
// the second element is the path for the js file.

const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
