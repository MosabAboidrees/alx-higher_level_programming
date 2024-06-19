#!/usr/bin/node
// A script that prints the first argument passed to it
const args = process.argv;
const firstArg = args[2] || 'No argument';
console.log(firstArg);
