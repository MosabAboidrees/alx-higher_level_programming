#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - Reverses the second half of the list
 * @head: Double pointer to the head of the list
 * Return: Pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_half, *prev_slow = *head;
	listint_t *midnode = NULL;  /*For lists with odd number of elements*/
	int result = 1;  /*Assume list is palindrome*/

	if (*head != NULL && (*head)->next != NULL)
	{
		/*Find the midpoint (slow will point to it at the end of loop)*/
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		/*For odd sized lists, skip the middle element*/
		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}
		/*Reverse the second half of the list*/
		second_half = slow;
		prev_slow->next = NULL;  /*Terminate first half*/
		reverse_listint(&second_half);
		result = compare_lists(*head, second_half);/*Check palindrome*/
		/*Restore the list*/
		reverse_listint(&second_half);  /*Reverse the second half again*/
		prev_slow->next = (midnode != NULL) ? midnode : second_half;
		if (midnode != NULL)
			midnode->next = second_half;
	}
	return (result);
}

/**
 * compare_lists - Compares two lists to check if they are equal
 * @head1: First list head
 * @head2: Second list head
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	/*Both lists are empty, or one is longer than the other*/
	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}
	return (0);
}
