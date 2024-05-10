#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: PyObject pointer to a Python object
 *
 * Description: This function checks if the provided PyObject is a string and
 * prints its type, length, and value. If the object is not a string, it prints
 * an error message with a specific format.
 */
void print_python_string(PyObject *p)
{
    /* Always start by printing the header for the string object info */
    printf("[.] string object info\n");

    /* Check if p is a valid pointer and is a Unicode string */
    if (!p || !PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Determine the type of string, compact ascii or compact unicode */
    const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";

    /* Get Unicode as UTF-8 */
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    PyObject *str_rep = PyUnicode_AsUTF8String(p);
    if (!str_rep) {
        PyErr_Print();
        return;
    }

    /* Print the detailed information about the string */
    char *utf8_string = PyBytes_AS_STRING(str_rep);
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", utf8_string);

    /* Decrement reference to the UTF-8 representation */
    Py_DECREF(str_rep);
}
