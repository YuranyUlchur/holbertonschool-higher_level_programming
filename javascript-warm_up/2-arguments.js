#!/usr/bin/node
// 'process.argv: contiene los argumentos pasados al'
// 'script en la línea de comandos'
// 'length: número total de elementos'

const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
