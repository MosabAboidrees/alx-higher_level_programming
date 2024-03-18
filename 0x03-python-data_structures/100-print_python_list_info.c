#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p); /*Get the size of the list*/
	Py_ssize_t alloc = ((PyListObject *)p)->allocated; /*Get the allocated size*/
	PyObject *item; /*Create a PyObject pointer*/
	Py_ssize_t i; /*Create a Py_ssize_t variable*/

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc); /*Print allocated size of the list*/

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i); /*Get item at index i*/
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name); /*Print item type*/
	}
}
