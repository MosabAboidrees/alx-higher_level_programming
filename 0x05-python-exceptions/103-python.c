#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>
/**
 * print_python_float - Prints information about Python float objects.
 * @p: Pointer to a PyObject structure.
 *
 * Description: This function checks if the given PyObject
 * is a float object and prints its value as a string.
 */
void print_python_float(PyObject *p)
{
	double float_value;

	/*Ensuring immediate output without buffering*/
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	/*Check if the object is of type float*/
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	/*Extract the float value from the PyObject*/
	float_value = ((PyFloatObject *)p)->ob_fval;
	/*Print the float value as a string*/
	printf("  value: %s\n", PyOS_double_to_string
	(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - Prints information about Python bytes objects.
 * @p: Pointer to a PyObject structure.
 *
 * Description: This function checks if the given PyObject is a bytes
 * object and prints its size, string content, and the first few bytes
 * in hexadecimal format.
 */
void print_python_bytes(PyObject *p)
{
	size_t byte_index, print_length, byte_size;
	char *byte_string;

	/*Ensuring immediate output without buffering*/
	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	/*Check if the object is of type bytes*/
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/*Extract size and string from the bytes object*/
	byte_size = ((PyVarObject *)p)->ob_size;
	byte_string = ((PyBytesObject *)p)->ob_sval;
	print_length = byte_size + 1 > 10 ? 10 : byte_size + 1;

	/*Print size and string content*/
	printf("  size: %lu\n", byte_size);
	printf("  trying string: %s\n", byte_string);
	/*Print the first few bytes in hexadecimal format*/
	printf("  first %lu bytes: ", print_length);
	for (byte_index = 0; byte_index < print_length; byte_index++)
	{
		printf("%02hhx%s", byte_string[byte_index],
		byte_index + 1 < print_length ? " " : "");
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about Python list objects.
 * @p: Pointer to a PyObject structure.
 *
 * Description: This function checks if the given PyObject is a list
 * object and prints its size, allocated space, and the type of each element.
 */
void print_python_list(PyObject *p)
{
	int element_index;
	Py_ssize_t list_size, allocated_size;

	/*Ensuring immediate output without buffering*/
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	/*Check if the object is of type list*/
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/*Extract size and allocated size from the list object*/
	list_size = ((PyVarObject *)p)->ob_size;
	allocated_size = ((PyListObject *)p)->allocated;
	/*Print size and allocated space*/
	printf("[*] Size of the Python List = %lu\n", list_size);
	printf("[*] Allocated = %lu\n", allocated_size);
	/*Iterate through list elements and print their type*/
	for (element_index = 0; element_index < list_size; element_index++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[element_index];
		printf("Element %d: %s\n", element_index, item->ob_type->tp_name);
		/*Print detailed info for bytes and float elements*/
		if (!strcmp(item->ob_type->tp_name, "bytes"))
			print_python_bytes(item);
		else if (!strcmp(item->ob_type->tp_name, "float"))
			print_python_float(item);
	}
}
