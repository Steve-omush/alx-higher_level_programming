#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head);
void reverse_list(listint_t **head);
int compare_lists(listint_t *head1, listint_t *head2);
/**
 * is_palindrome - checks if a singly linked list palindrome
 * @head: pointer to the head
 * Return: 1 if the linked list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid, *second_half;
	int is_palindrome = 1;

	slow = *head;
	fast = *head;
	mid = NULL;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		reverse_list(&second_half);
		is_palindrome = compare_lists(*head, second_half);
		reverse_list(&second_half);

		if (mid != NULL)
		{
			prev_slow->next = mid;
			mid->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head
 * Return: pointer to the new head
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - compares two linked list
 * @head1: pointer to the head of the first linked list
 * @head2: pointer to the head of the second linked list
 * Return: 1 if the linked lists are equal
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (1);
}
