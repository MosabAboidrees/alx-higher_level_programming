#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#include <floatobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list
 *
 * Description: This function prints the size of the list, the allocated space,
 * and the type of each element in the list. It checks if the object is a valid
 * PyListObject before proceeding.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated;
	PyObject *item;

	printf("[*] Python list info\n");
	/*Check if the object is a valid list*/
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/*Get the size of the list and allocated space*/
	size = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	/*Print size and allocated space*/
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	/*Iterate over the list items and print their types*/
	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}


/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject (bytes object)
 *
 * Description: This function prints the size of the bytes object, attempts
 * to print it as a string, and prints the first 10 bytes of the object.
 * It checks if the object is a valid PyBytesObject before proceeding.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	/*Check if the object is a valid bytes object*/
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/*Get the size of the bytes object and the string representation*/
	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	/*Print size and the string*/
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	/*Print the first 10 bytes of the object*/
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 9; i++)
	{
		printf(" %02x", string[i] & 0xff);
	}
	if (size >= 10)
	{
		printf(" %02x", string[9] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject (float object)
 *
 * Description: This function prints the value of the float object.
 * It checks if the object is a valid PyFloatObject before proceeding.
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	/*Check if the object is a valid float object*/
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	/*Get the value of the float object*/
	value = PyFloat_AS_DOUBLE(p);
	printf("  value: %g\n", value);
}
