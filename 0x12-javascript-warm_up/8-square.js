#!/usr/bin/node

const fill = (Number(process.argv[2]));
if (isNaN(fill)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < fill; x++) {
    console.log('X'.repeat(fill));
  }
}
