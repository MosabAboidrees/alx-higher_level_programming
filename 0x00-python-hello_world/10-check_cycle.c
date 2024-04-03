#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* Initialize two pointers, slow and fast */
	listint_t *slow = list, *fast = list;

	/* Iterate through the list */
	while (fast && fast->next)
	{
		/* Move slow pointer by one node */
		slow = slow->next;
		/* Move fast pointer by two nodes */
		fast = fast->next->next;
		/* Check if the slow and fast pointers meet */
		if (slow == fast)
		{
			/* If they meet, cycle is found */
			return (1);
		}
	}
	/* If no cycle is found, return 0 */
	return (0);
}
