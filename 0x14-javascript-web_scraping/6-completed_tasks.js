#!/usr/bin/node
// Script to compute the number of tasks completed by user ID

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: No API URL provided');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    console.log(completedTasks);
  }
});

