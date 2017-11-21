.. _nxsl-class-description:

############## 
NXSL Functions
##############

This chapter descrbes available NXSL functions.

Function tables
===============

.. list-table:: 
   :header-rows: 1
   :widths: 60 60 60 60 60 60 60 

   * - Generic
     - Math
     - String-related
     - Data Collection
     - Object search
     - Object management
     - Network
   * - :ref:`classof <nxsl-classof>`
     - :ref:`abs <nxsl-abs>`
     - :ref:`ArrayToString <nxsl-ArrayToString>`
     - :ref:`CreateDCI <nxsl-CreateDCI>`
     - :ref:`FindNodeObject <nxsl-FindNodeObject>`
     - :ref:`BindObject <nxsl-BindObject>`
     - :ref:`AddrInRange <nxsl-AddrInRange>`
   * - :ref:`d2x <nxsl-d2x>`
     - :ref:`ceil <nxsl-ceil>`
     - :ref:`chr <nxsl-chr>`
     - :ref:`FindAllDCIs <nxsl-FindAllDCIs>`
     - :ref:`FindObject <nxsl-FindObject>`
     - :ref:`CreateContainer <nxsl-CreateContainer>`
     - :ref:`AddrInSubnet <nxsl-AddrInSubnet>`
   * - :ref:`exit <nxsl-exit>`
     - :ref:`exp <nxsl-exp>`
     - :ref:`format <nxsl-format>`
     - :ref:`FindDCIByDescription <nxsl-FindDCIByDescription>`
     - :ref:`GetInterfaceName <nxsl-GetInterfaceName>`
     - :ref:`CreateNode <nxsl-CreateNode>`
     - :ref:`gethostbyaddr <nxsl-gethostbyaddr>`
   * - :ref:`GetConfigurationVariable <nxsl-GetConfigurationVariable>`
     - :ref:`floor <nxsl-floor>`
     - :ref:`index <nxsl-index>`
     - :ref:`FindDCIByName <nxsl-FindDCIByName>`
     - :ref:`GetInterfaceObject <nxsl-GetInterfaceObject>`
     - :ref:`DeleteCustomAttribute <nxsl-DeleteCustomAttribute>`
     - :ref:`gethostbyname <nxsl-gethostbyname>`
   * - :ref:`inList <nxsl-inList>`
     - :ref:`log <nxsl-log>`
     - :ref:`left <nxsl-left>`
     - :ref:`GetAvgDCIValue <nxsl-GetAvgDCIValue>`
     - :ref:`GetNodeInterfaces <nxsl-GetNodeInterfaces>`
     - :ref:`DeleteObject <nxsl-DeleteObject>`
     - 
   * - :ref:`map <nxsl-map>`
     - :ref:`log10 <nxsl-log10>`
     - :ref:`length <nxsl-length>`
     - :ref:`GetDCIObject <nxsl-GetDCIObject>`
     - :ref:`GetNodeParents <nxsl-GetNodeParents>`
     - :ref:`GetCustomAttribute <nxsl-GetCustomAttribute>`
     - 
   * - :ref:`mapList <nxsl-mapList>`
     - :ref:`pow <nxsl-pow>`
     - :ref:`lower <nxsl-lower>`
     - :ref:`GetDCIRawValue <nxsl-GetDCIRawValue>`
     - :ref:`GetNodeTemplates <nxsl-GetNodeTemplates>`
     - :ref:`ManageObject <nxsl-ManageObject>`
     - 
   * - :ref:`max <nxsl-max>`
     - :ref:`round <nxsl-round>`
     - :ref:`ltrim <nxsl-ltrim>`
     - :ref:`GetDCIValue <nxsl-GetDCIValue>`
     - :ref:`GetObjectChildren <nxsl-GetObjectChildren>`
     - :ref:`RenameObject <nxsl-RenameObject>`
     - 
   * - :ref:`min <nxsl-min>`
     - 
     - :ref:`ord <nxsl-ord>`
     - :ref:`GetDCIValues <nxsl-GetDCIValues>`
     - :ref:`GetObjectParents <nxsl-GetObjectParents>`
     - :ref:`SetCustomAttribute <nxsl-SetCustomAttribute>`
     - 
   * - :ref:`random <nxsl-random>`
     - 
     - :ref:`right <nxsl-right>`
     - :ref:`GetDCIValueByDescription <nxsl-GetDCIValueByDescription>`
     - :ref:`GetAllNodes <nxsl-GetAllNodes>`
     - :ref:`SetInterfaceExpectedState <nxsl-SetInterfaceExpectedState>`
     - 
   * - :ref:`sleep <nxsl-sleep>`
     - 
     - :ref:`rindex <nxsl-rindex>`
     - :ref:`GetDCIValueByName <nxsl-GetDCIValueByName>`
     - 
     - :ref:`UnbindObject <nxsl-UnbindObject>`
     - 
   * - :ref:`trace <nxsl-trace>`
     - 
     - :ref:`rtrim <nxsl-rtrim>`
     - :ref:`GetMaxDCIValue <nxsl-GetMaxDCIValue>`
     - 
     - :ref:`UnmanageObject <nxsl-UnmanageObject>`
     - 
   * - :ref:`typeof <nxsl-typeof>`
     - 
     - :ref:`SplitString <nxsl-SplitString>`
     - :ref:`GetMinDCIValue <nxsl-GetMinDCIValue>`
     - 
     - 
     - 
   * - :ref:`x2d <nxsl-x2d>`
     - 
     - :ref:`substr <nxsl-substr>`
     - :ref:`GetSumDCIValue <nxsl-GetSumDCIValue>`
     - 
     - 
     - 
   * - 
     - 
     - :ref:`trim <nxsl-trim>`
     - :ref:`PushDCIData <nxsl-PushDCIData>`
     - 
     - 
     - 
   * - 
     - 
     - :ref:`upper <nxsl-upper>`
     - 
     - 
     - 
     - 


.. list-table:: 
   :header-rows: 1
   :widths: 60 60 60 60 60 60 

   * - Time-related
     - Cryptography
     - SNMP
     - Agent
     - Event Processing
     - Situations
   * - :ref:`gmtime <nxsl-gmtime>`
     - :ref:`md5 <nxsl-md5>`
     - :ref:`CreateSNMPTransport <nxsl-CreateSNMPTransport>`
     - :ref:`AgentReadList <nxsl-AgentReadList>`
     - :ref:`FindAlarmById <nxsl-FindAlarmById>`
     - :ref:`FindSituation <nxsl-FindSituation>`
   * - :ref:`localtime <nxsl-localtime>`
     - :ref:`sha1 <nxsl-sha1>`
     - :ref:`SNMPGet <nxsl-SNMPGet>`
     - :ref:`AgentReadParameter <nxsl-AgentReadParameter>`
     - :ref:`FindAlarmByKey <nxsl-FindAlarmByKey>`
     - :ref:`GetSituationAttribute <nxsl-GetSituationAttribute>`
   * - :ref:`SecondsToUptime <nxsl-SecondsToUptime>`
     - :ref:`sha256 <nxsl-sha256>`
     - :ref:`SNMPGetValue <nxsl-SNMPGetValue>`
     - :ref:`AgentReadTable <nxsl-AgentReadTable>`
     - :ref:`GetEventParameter <nxsl-GetEventParameter>`
     - 
   * - :ref:`strftime <nxsl-strftime>`
     - 
     - :ref:`SNMPSet <nxsl-SNMPSet>`
     - 
     - :ref:`PostEvent <nxsl-PostEvent>`
     - 
   * - :ref:`time <nxsl-time>`
     - 
     - :ref:`SNMPWalk <nxsl-SNMPWalk>`
     - 
     - :ref:`SetEventParameter <nxsl-SetEventParameter>`
     - 
   * - :ref:`mktime <nxsl-mktime>`
     - 
     - 
     - 
     - 
     - 


Generic
=======

.. _nxsl-classof:

classof
-------

Returns the class name for given object.


Syntax
~~~~~~

classof(object);


Parameters
~~~~~~~~~~



 object 
 Object to get class name for.


Return Value
~~~~~~~~~~~~

Object's class name. If parameter passed to this function is not an object, runtime error will be generated.


Examples
~~~~~~~~

classof($node)		->	"Node"




.. _nxsl-d2x:

d2x
---

Returns the hexidecimal value of a decimal.


Syntax
~~~~~~

d2x(number [,padding]);


Parameters
~~~~~~~~~~



 number 
 Number to convert to hexadecimal value.


 padding 
 [Optional] left pads results to length given, must be a non-negative whole number.


Return Value
~~~~~~~~~~~~

Hexadecimal value of number.


Examples
~~~~~~~~

d2x(15)  	->	"F"
d2x(15,4)	->	"000F"




.. _nxsl-exit:

exit
----

Exit from script. This function never returns.


Syntax
~~~~~~

exit(code);


Parameters
~~~~~~~~~~



 code 
 Exit code (optional, 0 will be used by default).


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

 exit();    // exit with code 0
 exit(42);  // exit with code 42



.. _nxsl-GetConfigurationVariable:

GetConfigurationVariable
------------------------

Get value of server's configuration variable.


Since: 1.2.2


Syntax
~~~~~~

GetConfigurationVariable(variableName, [defaultValue])


Parameters
~~~~~~~~~~



 variableName 
 Server's configuration variable name.


 defaultValue 
 Default value to be returned if given variable is not set. If omited, NULL will be used as default value.


Return Value
~~~~~~~~~~~~

Value of requested variable or specified default value if given variable is not set.


Examples
~~~~~~~~

GetConfigurationVariable("NumberOfStatusPollers")			-> "10"
GetConfigurationVariable("BadVariable")				-> NULL
GetConfigurationVariable("BadVariable", 22)				-> "22"




.. _nxsl-inList:

inList
------

Check if given value is an element of given list.


Since: 1.2.14


Syntax
~~~~~~

inList(string, separator, value);


Parameters
~~~~~~~~~~



 string 
 String containing list of elements.


 separator 
 Element separator (can consist of multiple characters).


 value 
 Value to check.


Return Value
~~~~~~~~~~~~

TRUE if given value is an element of given list, FALSE otherwise.


Examples
~~~~~~~~

 inList("a,b,c", ",", "a");                              // TRUE
 inList("alpha::beta,gamma::delta", "::", "beta");       // FALSE
 inList("alpha::beta,gamma::delta", "::", "beta,gamma"); // TRUE
 inList("alpha::beta,gamma::delta", ",", "alpha::beta"); // TRUE



.. _nxsl-map:

map
---

Returns the value which corresponds to a specified key from specified Mapping Table


Syntax
~~~~~~

map(tableName, keyName);


Parameters
~~~~~~~~~~



 tableName 
 name of Mapping Table.


 keyName 
 name of the Key.


Return Value
~~~~~~~~~~~~

Value corresponding for a keyName from tableName.


Examples
~~~~~~~~

MyTable:


| MyKey1 | MyValue1 |
| MyKey2 | MyValue2 |


map("MyTable", "MyKey1")		->	returns "MyValue1"


myTable = "MyTable";
myKey = "MyKey1";
map(myTable, myKey)		->	returns "MyValue1"




.. _nxsl-mapList:

mapList
-------

Under construction

.. _nxsl-max:

max
---

Returns maximal value from a list of values.


Syntax
~~~~~~

max(number1 [,number2] [,number n]);


Parameters
~~~~~~~~~~



 numbers - separated by comma


Return Value
~~~~~~~~~~~~

Maximal value of numbers.


Examples
~~~~~~~~

max(2, 3, 4, 8)	->	8




.. _nxsl-min:

min
---

Returns minimal value from a list of values.


Syntax
~~~~~~

min(number1 [,number2] [,number n]);


Parameters
~~~~~~~~~~



 numbers - separated by comma


Return Value
~~~~~~~~~~~~

Minimal value of numbers.


Examples
~~~~~~~~

min(2, 3, 4, 8)	->	2




.. _nxsl-random:

random
------

Generate pseudo random number in given range. Uses c/c++ rand() function.


Syntax
~~~~~~

random(minValue, maxValue);


Parameters
~~~~~~~~~~



 minValue 
 start of range.


 maxValue 
 end of range.


Return Value
~~~~~~~~~~~~

Random value in range minValue..maxValue.


Examples
~~~~~~~~

random(0, 100)		->	random value in 0..100 range




.. _nxsl-sleep:

sleep
-----

Suspend script execution for given number of milliseconds.


Since: 1.2.2


Syntax
~~~~~~

sleep(milliseconds)


Parameters
~~~~~~~~~~



 milliseconds 
 Number of milliseconds to suspend script execution for.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

sleep(1000);   // sleep for 1 second



.. _nxsl-trace:

trace
-----

Writes message to netxms main log at given debug level.


Syntax
~~~~~~

trace(debugLevel, message);


Parameters
~~~~~~~~~~



 debugLevel 
 debug level in range 0..9.


 message 
 message text.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

trace(9, "my very important message")		->	add message to netxms log if netxms started with debug level 9
trace(6, "my very important message")		->	add message to netxms log if netxms started with debug level 6 or higher




.. _nxsl-typeof:

typeof
------

Returns the data type for given value.


Syntax
~~~~~~

typeof(value);


Parameters
~~~~~~~~~~



 value 
 Object to get data type for.


Return Value
~~~~~~~~~~~~

data type for given value. Type is returned as lowercase string. The following type names can be returned:


Examples
~~~~~~~~

typeof("abc")		->	"string"
typeof(17)		->	"int32"
typeof(17000000000)	->	"int64"
typeof($node)		->	"object"




.. _nxsl-x2d:

x2d
---

Returns the decimal value of a hexadecimal.


Syntax
~~~~~~

x2d(hex-number);


Parameters
~~~~~~~~~~



 hex-number 
 Hexadecimal number to convert to decimal value.


Return Value
~~~~~~~~~~~~

Decimal value of hex-number.


Examples
~~~~~~~~

x2d("10")  	->	16
x2d("1a")	->	26




Math
====

.. _nxsl-abs:

abs
---

Returns the absolute value of number.


Syntax
~~~~~~

abs(number);


Parameters
~~~~~~~~~~



 number 
 Number for which to return absolute value.


Return Value
~~~~~~~~~~~~

Absolute value of number.


Examples
~~~~~~~~

abs(12.3)	->	12.3
abs(-0.307)	->	0.307




.. _nxsl-ceil:

ceil
----

Round up value.


Since: 1.2.5


Syntax
~~~~~~

ceil(x);


Parameters
~~~~~~~~~~



 x 
 Floating point value.


Return Value
~~~~~~~~~~~~

The smallest integral value that is not less than x.


Examples
~~~~~~~~

ceil(2.3)	->	3
ceil(3.8)	->	4
ceil(-2.3)	->	-2
ceil(-3.8)	->	-3




.. _nxsl-exp:

exp
---

Returns e (the base of natural logarithms) raised to a power


Syntax
~~~~~~

exp(power);


Parameters
~~~~~~~~~~



 power 
 Used to calculate epower.


Return Value
~~~~~~~~~~~~

epower expressed as a real number.


Examples
~~~~~~~~

exp(2)		->	7.3890561




.. _nxsl-floor:

floor
-----

Round down value.


Since: 1.2.5


Syntax
~~~~~~

floor(x);


Parameters
~~~~~~~~~~



 x 
 Floating point value.


Return Value
~~~~~~~~~~~~

The largest integral value not greater than x.


Examples
~~~~~~~~

floor(2.3)	->	2
floor(3.8)	->	3
floor(-2.3)	->	-3
floor(-3.8)	->	-4




.. _nxsl-log:

log
---

Calculates natural logarithm of given value.


Syntax
~~~~~~

log(x);


Parameters
~~~~~~~~~~



 x 
 input value


Return Value
~~~~~~~~~~~~

Natural logarithm of x.


Examples
~~~~~~~~

log(2)		->	0.693147




.. _nxsl-log10:

log10
-----

Calculates logarithm of given value to base 10.


Syntax
~~~~~~

log10(x);


Parameters
~~~~~~~~~~



 x 
 input value


Return Value
~~~~~~~~~~~~

Logarithm of x to base 10.


Examples
~~~~~~~~

log10(2)	->	0.301030




.. _nxsl-pow:

pow
---

Calculates x raised to the power of y.


Syntax
~~~~~~

pow(x, y);


Parameters
~~~~~~~~~~



 x 
 Initial value.


 y 
 Power.


Return Value
~~~~~~~~~~~~

x raised to the power of y.


Examples
~~~~~~~~

pow(2, 3)	->	8




.. _nxsl-round:

round
-----

Round floating point value to the nearest integral value or floating point value with given precision.


Since: 1.2.5


Syntax
~~~~~~

round(x [, precision]);


Parameters
~~~~~~~~~~



 x 
 Floating point value.


 precision 
 optional number of decimal places to be left. If omited or set to 0, x will be rounded to integral value.


Return Value
~~~~~~~~~~~~

The integral value that is closest to x if precision is omited or set to 0, or floating point value rounded to have given number of decimal places.


Examples
~~~~~~~~

round(2.3)	 ->	2
round(3.8)	 ->	4
round(-2.3)	 ->	-2
round(-3.8)	 ->	-4
round(2.378, 2) ->	2.38
round(2.378, 1) ->	2.4




String-related
==============

.. _nxsl-ArrayToString:

ArrayToString
-------------

Concatenates array elements into single string. If some array elements are arrays, they will be concatenated recursively.


Since: 2.0.2


Syntax
~~~~~~

ArrayToString(array, separator);


Parameters
~~~~~~~~~~



 array 
 Array to convert.


 separator 
 Separator to be placed between elements. Can be empty string.


Return Value
~~~~~~~~~~~~

Array elements concatenated into single string.


Examples
~~~~~~~~

ArrayToString(%("hello", "world"), " ")	->	"hello world"
ArrayToString(%("1", "2", "3"), "")		->	"123"




.. _nxsl-chr:

chr
---

Return a character from it's UNICODE code.


Syntax
~~~~~~

chr(code);


Parameters
~~~~~~~~~~



 code 
 A character's UNICODE code.


Return Value
~~~~~~~~~~~~

A string consisting of single character.


Examples
~~~~~~~~

chr(50)	->	"P"




.. _nxsl-format:

format
------

Formats a numeric value.


Since: 1.2.5


Syntax
~~~~~~

format(number, width, precision);


Parameters
~~~~~~~~~~



 number 
 The numeric value to format.


 width 
 Minimum number of characters. If the number of characters in the output value is less than the specified width, blanks are added to the left or the right of the values — depending on whether the width is negative (for left alignment) or positive (for right alignment) — until the minimum width is reached. The width specification never causes a value to be truncated.


 precision 
 The number of decimal places. Floating point value will be rounded accordingly.


Return Value
~~~~~~~~~~~~

Formatted numeric value.


Examples
~~~~~~~~

format(3.7, 7, 2)		->	"   3.70"
format(3.7, -7, 2)		->	"3.70   "
format(5.7278, 1, 2)		->	"5.73"
format(5.7278, 1, 0)		->	"6"




.. _nxsl-index:

index
-----

Returns the position of the first occurrence of substring in string at or after position if specifed.


Syntax
~~~~~~

index(string, substring [,position]);


Parameters
~~~~~~~~~~



 string 
 The string which will be examined.


 substring 
 The string which we will search for.


 position 
 [Optional] The starting position in the string to begin our search from the left.


All index values are 1-based (i.e. the first character has index 1, not 0).


Return Value
~~~~~~~~~~~~

Integer value of the position substring was found at, will return 0 if not found.


Examples
~~~~~~~~

index("abcdef","cd")  	        ->	3
index("abcdef","cd",4)  	->	0
index("abcdefabcdef","cd",4)	->	9




.. _nxsl-left:

left
----

Returns the string of length characters of string, optionally padded with pad character instead of a blank (space).


Syntax
~~~~~~

left(string, length [,pad]);


Parameters
~~~~~~~~~~



 string 
 The string which will be processed.


 length 
 The number of character to return, must be a positive integer.


 pad 
 [Optional] The pad character to use instead of blank spaces.


Return Value
~~~~~~~~~~~~

String of the left length characters.


Examples
~~~~~~~~

left("abc d",8)  	->	"abc d   "
left("abc d",8,".")  	->	"abc d..."
left("abc  def",7)	->	"abc  de"




.. _nxsl-length:

length
------

Returns the length of string.


Syntax
~~~~~~

length(string);


Parameters
~~~~~~~~~~



 string 
 The string to determine its length.


Return Value
~~~~~~~~~~~~

Integer length of the string passed to the function.


Examples
~~~~~~~~

length("abcd")  	->	4




.. _nxsl-lower:

lower
-----

Converts string to lowercase.


Syntax
~~~~~~

lower(string);


Parameters
~~~~~~~~~~



 string 
 The string to convert.


Return Value
~~~~~~~~~~~~

Source string converted to lowercase.


Examples
~~~~~~~~

lower("aBcD")  	->	"abcd"




.. _nxsl-ltrim:

ltrim
-----

Removes blanks (space and tab characters) from the left side of specified string.


Syntax
~~~~~~

ltrim(string);


Parameters
~~~~~~~~~~



 string 
 Source string.


Return Value
~~~~~~~~~~~~

Source string with blanks at the left side removed.


Examples
~~~~~~~~

ltrim("  abc def  ")  	->	"abc def  "




.. _nxsl-ord:

ord
---

Convert a character into it's ASCII/Unicode value.


Only processes one character.


Syntax
~~~~~~

ord(character);


Parameters
~~~~~~~~~~



 character 
 A character to convert.


Return Value
~~~~~~~~~~~~

An ASCII/Unicode value


Examples
~~~~~~~~

ord("a")	->	97
ord("abc")	->	97




.. _nxsl-right:

right
-----

Returns the string of length characters of string, optionally padded with pad character instead of blank (space) starting from the right.  Padding occurs on the left portion of the string.


Syntax
~~~~~~

right(string, length [,pad]);


Parameters
~~~~~~~~~~



 string 
 The string which will be processed.


 length 
 The number of character to return, must be a positive integer.


 pad 
 [Optional] The pad character to use instead of blank spaces.


Return Value
~~~~~~~~~~~~

String of the right length characters.


Examples
~~~~~~~~

right("abc  d",8)  	->	"  abc  d"
right("abc def",5)  	->	"c def"
right("17",5,"0")	->	"00017"




.. _nxsl-rindex:

rindex
------

Returns the position of the last occurrence of substring in string up to or before position if specifed.


Syntax
~~~~~~

rindex(string, substring [,position]);


Parameters
~~~~~~~~~~



 string 
 The string which will be examined.


 substring 
 The string which we will search for.


 position 
 [Optional] The position in string to start searching back from.


All index values are 1-based (i.e. the first character has index 1, not 0).


Return Value
~~~~~~~~~~~~

Integer value of the position substring was found at, will return 0 if not found.


Examples
~~~~~~~~

rindex("abcdabcd","cd")  	      ->	7
rindex("abcdef","cd",2)  	      ->	0
rindex("abcdefabcdef","cd",4)	      ->	3




.. _nxsl-rtrim:

rtrim
-----

Removes blanks (space and tab characters) from the right side of specified string.


Syntax
~~~~~~

rtrim(string);


Parameters
~~~~~~~~~~



 string 
 Source string.


Return Value
~~~~~~~~~~~~

Source string with blanks at the right side removed.


Examples
~~~~~~~~

rtrim("  abc def  ")  	->	"  abc def"




.. _nxsl-SplitString:

SplitString
-----------

Split string into array of strings at given separator.


Since: 2.0.3


Syntax
~~~~~~

SplitString(string, separator);


Parameters
~~~~~~~~~~



 string 
 String to split.


 separator 
 Separator character. If supplied string is longer than 1 character, it's first character will be used as separator.


Return Value
~~~~~~~~~~~~

Array of strings.


Examples
~~~~~~~~

format("a;b;c;d", ";")		->	%("a", "b", "c", "d")
format("abcd", ";")		->	%("abcd")




.. _nxsl-substr:

substr
------

Extracts the substring from string that begins at the nth character and is of length len.


Syntax
~~~~~~

substr(string, n[, len]);


Parameters
~~~~~~~~~~



 string 
 Source string.


 n 
 Starting character index for substring. The n must be a positive whole number.  If n is greater than length(string), then empty string is returned.


 len 
 Length of substring. If you omit length, the rest of the string is returned.


Return Value
~~~~~~~~~~~~

Extracted substring.


Examples
~~~~~~~~

substr("abcdef", 3, 2)		->	"cd"
substr("abcdef", 8)		->	""
substr("abcdef", 4)		->	"def"




.. _nxsl-trim:

trim
----

Removes blanks (space and tab characters) from both sides of specified string.


Syntax
~~~~~~

trim(string);


Parameters
~~~~~~~~~~



 string 
 Source string.


Return Value
~~~~~~~~~~~~

Source string with blanks at both sides removed.


Examples
~~~~~~~~

trim("  abc def  ")  	->	"abc def"




.. _nxsl-upper:

upper
-----

Converts string to uppercase.


Syntax
~~~~~~

upper(string);


Parameters
~~~~~~~~~~



 string 
 The string to convert.


Return Value
~~~~~~~~~~~~

Source string converted to uppercase.


Examples
~~~~~~~~

upper("aBcD")  	->	"ABCD"




Data Collection
===============

.. _nxsl-CreateDCI:

CreateDCI
---------

Create new DCI.


Since: 1.2.6


Syntax
~~~~~~

CreateDCI(node, source, name, description, dataType, pollingInterval, retentionTime);


Parameters
~~~~~~~~~~



 node 
 Node object to create DCI on.


 source 
 Data collection source. Should be on of:


 "agent" 
 source is NetXMS agent.


 "internal" 
 source is server's internal data.


 "push" 
 source is push agent.


 "snmp" 
 source is SNMP agent.



 name 
 Metric name (parameter for agent and internal DCIs, OID for SNMP).


 description 
 Textual description of the DCI.


 dataType 
 DCI data type. Should be one of:


 "int32" 
 signed 32-bit integer.


 "uint32" 
 unsigned 32-bit integer.


 "int64" 
 signed 64-bit integer.


 "uint64" 
 unsigned 64-bit integer.


 "float" 
 floating point number.


 "string" 
 text string.



 pollingInterval 
 Interval in seconds between polls.


 retentionTime 
 DCI retention time in days.


Return Value
~~~~~~~~~~~~

DCI object on success or null on failure.


Examples
~~~~~~~~

// Create DCI to collect agent's version every 300 seconds and
// keep history for 370 days on node named "SERVER"
node = FindNodeObject(null, "SERVER");
if (node != null)
{
	dci = CreateDCI(node, "agent", "Agent.Version", "Version of NetXMS agent", "string", 300, 370);
	println (dci != null) ? "DCI created" : "DCI creation failed";
}
else
{
	println "Cannot find node object";
}



.. _nxsl-FindAllDCIs:

FindAllDCIs
-----------

Find all DCIs with matching name or description on given node.


Since: 1.2.12


Syntax
~~~~~~

FindAllDCIs(node, nameFilter, descriptionFilter);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 nameFilter 
 Filter for DCI names (* and ? metacharacters can be used). If omitted all names will be matched.


 descriptionFilter 
 Filter for DCI names (* and ? metacharacters can be used). If omitted all names will be matched.


Return Value
~~~~~~~~~~~~

Array of DCI objects. If no matching objects found empty array will be returned.


Examples
~~~~~~~~

FindAllDCIs($node, "System.CPU.Usage(*)"); // Find System.CPU.Usage() parameters for all CPUs




.. _nxsl-FindDCIByDescription:

FindDCIByDescription
--------------------

Find DCI by description (search is case-insensetive).


Syntax
~~~~~~

FindDCIByDescription(node, description);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 description 
 DCI description.


Return Value
~~~~~~~~~~~~

DCI ID on success or 0 if DCI with matching description was not found.


Examples
~~~~~~~~

FindDCIByDescription($node, "Status")	-> 4   /* perhaps */
FindDCIByDescription($node, "bad dci")	-> 0




.. _nxsl-FindDCIByName:

FindDCIByName
-------------

Find DCI by name (search is case-insensetive).


Syntax
~~~~~~

FindDCIByName(node, description);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 name 
 DCI name.


Return Value
~~~~~~~~~~~~

DCI ID on success or 0 if DCI with matching name was not found.


Examples
~~~~~~~~

FindDCIByName($node, "Agent.Uptime")	-> 5   /* perhaps */
FindDCIByName($node, "bad")		-> 0




.. _nxsl-GetAvgDCIValue:

GetAvgDCIValue
--------------

Get the average value of the DCI for the given period. The DCI value must be of numeric type.


Since: 1.2.1


Syntax
~~~~~~

GetAvgDCIValue(node, dciId, from, to);


Parameters
~~~~~~~~~~



 node 
 Node object to calculate the average DCI value for.


 dciId 
 DCI item id (integer).


 from 
 Start of the period (as UNIX timestamp).


 to 
 End of the period (as UNIX timestamp).


Return Value
~~~~~~~~~~~~

Average value or null on failure.


Examples
~~~~~~~~

sub main()
{
    value = GetAvgDCIValue(FindObject("MYWORKPC"), 18, 0, time()); // from the beginning till now
    trace(1, "Processor average load ". value . "%");
}



.. _nxsl-GetDCIObject:

GetDCIObject
------------

Get DCI object with given ID.


Syntax
~~~~~~

GetDCIObject(node, id);


Parameters
~~~~~~~~~~



 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null as node if trusted nodes check is disabled (see Security Issues for more information).


 id 
  DCI id on node.


Return Value
~~~~~~~~~~~~

DCI object with given id on success or null on failure (if object with given id does not exist, or access to it was denied).


Examples
~~~~~~~~

GetDCIObject($node, 2)	                -> object
GetDCIObject($node, bad_id)		-> NULL




.. _nxsl-GetDCIRawValue:

GetDCIRawValue
--------------

Get last raw value (before transformation) of DCI with given ID on given node.


Since: 1.2.8


Syntax
~~~~~~

GetDCIRawValue(node, id);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 id 
 DCI ID.


Return Value
~~~~~~~~~~~~

Last raw value (before transformation) for given DCI or null if DCI with given ID does not exist or has no collected values.


Examples
~~~~~~~~

GetDCIRawValue($node, FindDCIByName($node, "Status"))	->	0




.. _nxsl-GetDCIValue:

GetDCIValue
-----------

Get last value of DCI with given ID on given node.


Syntax
~~~~~~

GetDCIValue(node, id);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 id 
 DCI ID.


Return Value
~~~~~~~~~~~~

Last value for given DCI (string for normal DCIs and Table object for table DCIs) or null if DCI with given ID does not exist or has no collected values.


Examples
~~~~~~~~

GetDCIValue($node, FindDCIByName($node, "Status"))	->	0




.. _nxsl-GetDCIValues:

GetDCIValues
------------

Get all values for period of DCI with given ID on given node.


Since: 1.2.10


Syntax
~~~~~~

GetDCIValues(node, id, startTime, endTime);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 id 
 DCI ID.


 startTime 
 Start of the period (as UNIX timestamp).


 endTime 
 End of the period (as UNIX timestamp).


Return Value
~~~~~~~~~~~~

Array of value ordered from latest to earliest for given DCI or null if DCI with given ID does not exist or has no collected values. This function cannot be used for table DCIs.


Examples
~~~~~~~~

GetDCIValues($node, FindDCIByName($node, "Status"), time() - 3600, time()); // Values for last hour




.. _nxsl-GetDCIValueByDescription:

GetDCIValueByDescription
------------------------

Get last value of DCI with given description on given node.


Syntax
~~~~~~

GetDCIValueByDescription(node, description);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 description 
 DCI description.


Return Value
~~~~~~~~~~~~

Last value for given DCI (string for normal DCIs and Table object for table DCIs) or null if DCI with given description does not exist or has no collected values.


Examples
~~~~~~~~

GetDCIValueByDescription($node, "Status")	->	0




.. _nxsl-GetDCIValueByName:

GetDCIValueByName
-----------------

Get last value of DCI with given name on given node.


Syntax
~~~~~~

GetDCIValueByName(node, name);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


 name 
 DCI name (parameter's name for agent or internal source, and OID for SNMP source).


Return Value
~~~~~~~~~~~~

Last value for given DCI (string for normal DCIs and Table object for table DCIs) or null if DCI with given name does not exist or has no collected values.


Examples
~~~~~~~~

GetDCIValueByName($node, "Agent.Version")	->	"1.2.0"




.. _nxsl-GetMaxDCIValue:

GetMaxDCIValue
--------------

Get the maximum value of the DCI for the given period. The DCI value must be of numeric type.


Since: 1.2.1


Syntax
~~~~~~

GetMaxDCIValue(node, dciId, from, to);


Parameters
~~~~~~~~~~



 node 
 Node object to calculate the maximum DCI value for.


 dciId 
 DCI item id (integer).


 from 
 Start of the period (as UNIX timestamp).


 to 
 End of the period (as UNIX timestamp).


Return Value
~~~~~~~~~~~~

Maximum value or null on failure.


Examples
~~~~~~~~

sub main()
{
    value = GetMaxDCIValue(FindObject("MYWORKPC"), 18, 0, time()); // from the beginning till now
    trace(1, "Processor max load ". value . "%");
}



.. _nxsl-GetMinDCIValue:

GetMinDCIValue
--------------

Get the minimum value of the DCI for the given period. The DCI value must be of numeric type.


Since: 1.2.1


Syntax
~~~~~~

GetMinDCIValue(node, dciId, from, to);


Parameters
~~~~~~~~~~



 node 
 Node object to calculate the mininum DCI value for.


 dciId 
 DCI item id (integer).


 from 
 Start of the peridod (as UNIX timestamp).


 to 
 End of the peridod (as UNIX timestamp).


Return Value
~~~~~~~~~~~~

Minimum value or null on failure.


Examples
~~~~~~~~

sub main()
{
    value = GetMinDCIValue(FindObject("MYWORKPC"), 18, 0, time()); // from the beginning till now
    trace(1, "Processor minimum load ". value . "%");
}



.. _nxsl-GetSumDCIValue:

GetSumDCIValue
--------------

Get the sum value of the DCI for the given period. The DCI value must be of numeric type.


Since: 1.2.7


Syntax
~~~~~~

GetSumDCIValue(node, dciId, from, to);


Parameters
~~~~~~~~~~



 node 
 Node object to calculate the sum DCI value for.


 dciId 
 DCI item id (integer).


 from 
 Start of the peridod (as UNIX timestamp).


 to 
 End of the peridod (as UNIX timestamp).


Return Value
~~~~~~~~~~~~

Sum value or null on failure.


Examples
~~~~~~~~

sub main()
{
    value = GetSumDCIValue(FindObject("MYWORKPC"), 18, 0, time()); // from the beginning till now
    trace(1, "Processor sum load ". value . "%");
}



.. _nxsl-PushDCIData:

PushDCIData
-----------

Push new DCI value from script. 


Since: 2.0-M1


Syntax
~~~~~~

PushDCIData(node, dciId, value);


Parameters
~~~~~~~~~~



 node 
 Node object containing required DCI.


 dciId 
 DCI id for which new value will be pushed (DCI source must be set to "Push").


 value 
 New value for DCI.


Return Value
~~~~~~~~~~~~

No return value


Examples
~~~~~~~~

   PushDCIData($node, 46, 13);



Object search
=============

.. _nxsl-FindNodeObject:

FindNodeObject
--------------

Find node object by node id or node name.


Syntax
~~~~~~

FindNodeObject(node, id);


Parameters
~~~~~~~~~~



 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null as node if trusted nodes check is disabled (see Security Issues for more information).


 id 
 ID or name of the node to find.


Return Value
~~~~~~~~~~~~

Node object with given id or name on success or null on failure (either because node with given name/id does not exist, or access to it was denied).


Examples
~~~~~~~~

FindNodeObject($node, "server.netxms.org")	-> object
FindNodeObject(null, 12)			-> object
FindNodeObject($node, "bad_node_name")		-> NULL




.. _nxsl-FindObject:

FindObject
----------

Find NetXMS object by object id or name.


Since: 1.2.0


Syntax
~~~~~~

FindObject(id, node);


Parameters
~~~~~~~~~~



 id 
 ID or name of the object to find.


 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null or omit this parameter if trusted nodes check is disabled (see Security Issues for more information).


Return Value
~~~~~~~~~~~~

Object of NetObj or one of its sub-clases (depending on found object type) with given id or name on success or null on failure (either because object with given name/id does not exist, or access to it was denied).
For more info see NXSL Class Reference.


Examples
~~~~~~~~

FindObject("server.netxms.org", $node)	-> object
FindObject(2)				-> object
FindObject("bad_object_name", $node)	-> NULL




.. _nxsl-GetInterfaceName:

GetInterfaceName
----------------

Get interface name by index.


Syntax
~~~~~~

GetInterfaceName(obj, index);


Parameters
~~~~~~~~~~



 obj 
 A node object.


 index 
 An interface index.


Return Value
~~~~~~~~~~~~

Name of the requested interface or null if not found.


Examples
~~~~~~~~

GetInterfaceName($node, 2);	->	ether1
GetInterfaceName($node, 55);	->	null




.. _nxsl-GetInterfaceObject:

GetInterfaceObject
------------------

Get interface object by index.


Syntax
~~~~~~

GetInterfaceObject(obj, index);


Parameters
~~~~~~~~~~



 obj 
 A node object.


 index 
 An interface index.


Return Value
~~~~~~~~~~~~

An interface object, or null if not found.


Examples
~~~~~~~~

GetInterfaceObject($node, 2);		->	interface object
GetInterfaceObject($node, 55);		->	null




.. _nxsl-GetNodeInterfaces:

GetNodeInterfaces
-----------------

Get all interfaces for given node.


Since: 1.2.0


Syntax
~~~~~~

GetNodeInterfaces(node);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


Return Value
~~~~~~~~~~~~

Array of objects of class Interface, with first object placed at index 0. End of list indicated by array element with null value.


Examples
~~~~~~~~

// Log names and ids of all interface objects for given node
interfaces = GetNodeInterfaces($node);
foreach(i : interfaces)
{
	trace(1, "Interface: name='" . i->name . "' id=" . i->id);
}



.. _nxsl-GetNodeParents:

GetNodeParents
--------------

Get accessible parent objects for given node.


Since: 1.0.8


Syntax
~~~~~~

GetNodeParents(node);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


Return Value
~~~~~~~~~~~~

Array of objects of class NetObj (generic NetXMS object), with first object placed at index 0. End of list indicated by array element with null value.  Return value also affected by trusted nodes settings (see Security Issues for more information).
This function will never return template or policy objects applied to node.
Objects of these types will be returned:
OBJECT_CONTAINER
OBJECT_CLUSTER
OBJECT_SUBNET
OBJECT_SERVICEROOT


Examples
~~~~~~~~

// Log names and ids of all accessible parents for current node
parents = GetNodeParents($node);
foreach(p : parents)
{
	trace(1, "Parent object: name='" . p->name . "' id=" . p->id);
}



.. _nxsl-GetNodeTemplates:

GetNodeTemplates
----------------

Get accessible template objects for given node.


Since: 2.0-M1


Syntax
~~~~~~

GetNodeTemplates(node);


Parameters
~~~~~~~~~~



 node 
 Node object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


Return Value
~~~~~~~~~~~~

Array of objects, with first object placed at index 0. End of list indicated by array element with null value.  Return value also affected by trusted nodes settings (see Security Issues for more information).
This function will only return template objects applied to node with the object type:
OBJECT_TEMPLATE


Examples
~~~~~~~~

// Log names and ids of all accessible templates for current node
templates = GetNodeTemplates($node);
foreach(t : templates)
{
	trace(1, "Template object: name='" . t->name . "' id=" . t->id);
}



.. _nxsl-GetObjectChildren:

GetObjectChildren
-----------------

Get accessible child objects for given object.


Since: 1.2.2


Syntax
~~~~~~

GetObjectChildren(object);


Parameters
~~~~~~~~~~



 object 
 Node, Interface, or NetObj object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


Return Value
~~~~~~~~~~~~

Array of objects of class Node, Interface, or NetObj, with first object placed at index 0. End of list indicated by array element with null value. Return value also affected by trusted nodes settings (see Security Issues for more information).


Examples
~~~~~~~~

// Log names and ids of all accessible child objects for current node
children = GetObjectChildren($node);
foreach(p : children)
{
	trace(1, "Child object: name='" . p->name . "' id=" . p->id);
}



.. _nxsl-GetObjectParents:

GetObjectParents
----------------

Get accessible parent objects for given object.


Since: 1.2.2


Syntax
~~~~~~

GetObjectParents(object);


Parameters
~~~~~~~~~~



 object 
 Node, Interface, or NetObj object. Predefined variable $node can be used to refer to current node in transformation script or event processing policy rule.


Return Value
~~~~~~~~~~~~

Array of objects of class NetObj (generic NetXMS object), with first object placed at index 0. End of list indicated by array element with null value. This function will never return template or policy objects applied to node. Return value also affected by trusted nodes settings (see Security Issues for more information).


Examples
~~~~~~~~

// Log names and ids of all accessible parents for current node
parents = GetObjectParents($node);
foreach(p : parents)
{
	trace(1, "Parent object: name='" . p->name . "' id=" . p->id);
}



.. _nxsl-GetAllNodes:

GetAllNodes
-----------

Under construction

Object management
=================

.. _nxsl-BindObject:

BindObject
----------

Bind all NetXMS objects that can be bound from console (nodes, subnets, clusters, and another containers) to container objects.


Since: 1.2.0


Syntax
~~~~~~

BindObject(parent, child);


Parameters
~~~~~~~~~~



 parent 
 Parent object (NetObj referring to container object or infrastructure service root).


 child 
 The NetXMS object to be linked to given parent object (Node or NetObj referring to subnet, container, or cluster).


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

BindObject(FindObject(2), $node);    // Link current node directly to "Infrastructure Services"
BindObject(FindObject("Services"), FindObject("Service_1"));    // Link object named "Service_1" to container "Services"



.. _nxsl-CreateContainer:

CreateContainer
---------------

Create container object.


Since: 1.2.0


Syntax
~~~~~~

CreateContainer(parent, name);


Parameters
~~~~~~~~~~



 parent 
 Parent object. Can be either container or infrastructure services root. Reference to parent object can be obtained using FindObject function.


 name 
 Name for new container object.


Return Value
~~~~~~~~~~~~

Reference to newly created object.


Examples
~~~~~~~~

 CreateContainer(FindObject(2), "New Container");    // Create container directly under "Infrastructure Services"



.. _nxsl-CreateNode:

CreateNode
----------

Create node object.


Since: 1.2.7


Syntax
~~~~~~

CreateNode(parent, name, primaryHostName);


Parameters
~~~~~~~~~~



 parent 
 Parent object. Can be either container or infrastructure services root. Reference to parent object can be obtained using FindObject function.


 name 
 Name for new node object.


 primaryHostName 
 primary host name for new node object. Must be valid IP address or resolvable host name.


Return Value
~~~~~~~~~~~~

Reference to newly created object.


Examples
~~~~~~~~

 CreateNode(FindObject(2), "SERVER", "10.10.10.1");    // Create node directly under "Infrastructure Services"



.. _nxsl-DeleteCustomAttribute:

DeleteCustomAttribute
---------------------

Delete node's custom attribute.


Since: 1.2.17


Syntax
~~~~~~

DeleteCustomAttribute(node, attributeName)


Parameters
~~~~~~~~~~



 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null as node if trusted nodes check is disabled (see Security Issues for more information).


 attributeName 
 Custom attribute name.


Return Value
~~~~~~~~~~~~

null


Examples
~~~~~~~~

DeleteCustomAttribute($node, "my_attribute");



.. _nxsl-DeleteObject:

DeleteObject
------------

Delete object.


Since: 1.2.8


Syntax
~~~~~~

DeleteObject(object);


Parameters
~~~~~~~~~~



 object 
 NetXMS object to be deleted. Can be NXSL class NetObj, Node, or Interface. Reference to object can be obtained using FindObject function.


Return Value
~~~~~~~~~~~~

None.




.. _nxsl-GetCustomAttribute:

GetCustomAttribute
------------------

Get value of node's custom attribute.


Syntax
~~~~~~

GetCustomAttribute(node, attributeName)


Parameters
~~~~~~~~~~



 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null as node if trusted nodes check is disabled (see Security Issues for more information).


 attributeName 
 Custom attribute name.


Return Value
~~~~~~~~~~~~

String value of requested custom attribute or NULL if attribute is missing.


Notes
~~~~~

If attribute name conforms to NXSL identifier naming conventions, it can be accessed directly as node object attribute. For example “GetCustomAttribute($node, "my_attribute")” can be changed to “$node->my_attribute”. If custom attribute does not exist, accessing via "->" will generate error. Alternative way it to use syntax "my_attribute@$node", which will return NULL for missing attribute instead.


Examples
~~~~~~~~

GetCustomAttribute($node, "my_attribute")	-> "my value"
GetCustomAttribute($node, "bad_attribute_name")	-> NULL




.. _nxsl-ManageObject:

ManageObject
------------

Set object into managed state. Has no effect if object is already in managed state.


Since: 1.2.6


Syntax
~~~~~~

ManageObject(object);


Parameters
~~~~~~~~~~



 object 
 NetXMS object to be modified. Can be NXSL class NetObj, Node, or Interface. Reference to object can be obtained using FindObject function.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

 ManageObject(FindObject(2));    // Set "Infrastructure Services" object to managed state



.. _nxsl-RenameObject:

RenameObject
------------

Rename object.


Since: 1.2.3


Syntax
~~~~~~

RenameObject(object, name);


Parameters
~~~~~~~~~~



 object 
 NetXMS object to be renamed. Can be NXSL class NetObj, Node, or Interface. Reference to object can be obtained using FindObject function.


 name 
 New name for object.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

 RenameObject(FindObject(2), "My Services");    // Rename "Infrastructure Services" object



.. _nxsl-SetCustomAttribute:

SetCustomAttribute
------------------

Set value of node's custom attribute. If attribute was not defined, it will be created.


Since: 1.1.1


Syntax
~~~~~~

SetCustomAttribute(node, attributeName, value)


Parameters
~~~~~~~~~~



 node 
 Node object, you can use predefined variable $node to refer to current node. You can also use null as node if trusted nodes check is disabled (see Security Issues for more information).


 attributeName 
 Custom attribute name.


 value 
 New value for custom attribute.


Return Value
~~~~~~~~~~~~

Previous value of requested custom attribute or NULL if attribute was not defined before.


Examples
~~~~~~~~

SetCustomAttribute($node, "my_attribute", "new value")			-> "old value"
SetCustomAttribute($node, "non_existing_attribute", "new value")	-> NULL




.. _nxsl-SetInterfaceExpectedState:

SetInterfaceExpectedState
-------------------------

Set expected state for given interface.


Since: 1.2.6


Syntax
~~~~~~

SetInterfaceExpectedState(interface, state);


Parameters
~~~~~~~~~~



 interface 
 Interface object. Can be obtained using GetNodeInterfaces or GetInterfaceObject.


 state 
 New expected state for interface. Can be specified as integer code or state name. Possible values are:


 Code 
 Name


 0 
 UP


 1 
 DOWN


 2 
 IGNORE



Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

// Set expected state to "ignore" for all interfaces of given node
interfaces = GetNodeInterfaces($node);
foreach(i : interfaces)
{
	SetInterfaceExpectedState(i, "IGNORE");
}



.. _nxsl-UnbindObject:

UnbindObject
------------

Remove (unbind) object from a container.


Syntax
~~~~~~

UnbindObject(parent, child);


Parameters
~~~~~~~~~~



 parent 
 Parent object (NetObj referring to container object or infrastructure service root).


 child 
 The NetXMS object to be unlinked from given parent object (Node or NetObj referring to node, subnet, container, or cluster).


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

UnbindObject(FindObject("Services"), FindObject("Service_1"));    // Unlink object named "Service_1" from container "Services"



.. _nxsl-UnmanageObject:

UnmanageObject
--------------

Set object into unmanaged state. Has no effect if object is already in unmanaged state.


Since: 1.2.6


Syntax
~~~~~~

UnmanageObject(object);


Parameters
~~~~~~~~~~



 object 
 NetXMS object to be modified. Can be NXSL class NetObj, Node, or Interface. Reference to object can be obtained using FindObject function.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

 UnmanageObject(FindObject(2));    // Set "Infrastructure Services" object to unmanaged state



Network
=======

.. _nxsl-AddrInRange:

AddrInRange
-----------

Checks if given IP address is within given range (including both bounding addresses).


Syntax
~~~~~~

AddrInRange(address, start, end);


Parameters
~~~~~~~~~~



 address 
 IP address to check.


 start 
 Starting IP address of a range.


 end 
 Ending IP address of a range.


All IP addresses should be specified as strings.


Return Value
~~~~~~~~~~~~

TRUE if address is within given range (including both bounding addresses), and FALSE otherwise.


Examples
~~~~~~~~

AddrInRange("10.0.0.16", "10.0.0.2", "10.0.0.44")		->	TRUE
AddrInRange("10.0.0.16", "192.168.1.1", "192.168.1.100")	->	FALSE




.. _nxsl-AddrInSubnet:

AddrInSubnet
------------

Checks if given IP address is within given subnet (including subnet and broadcast addresses).


Syntax
~~~~~~

AddrInSubnet(address, subnet, mask);


Parameters
~~~~~~~~~~



 address 
 IP address to check.


 subnet 
 Subnet address.


 mask 
 Subnet mask.


All IP addresses should be specified as strings.


Return Value
~~~~~~~~~~~~

TRUE if address is within given subnet (including subnet and broadcast addresses), and FALSE otherwise.


Examples
~~~~~~~~

AddrInSubnet("10.0.0.16", "10.0.0.0", "255.255.255.0")		->	TRUE
AddrInSubnet("10.0.0.16", "192.168.1.0", "255.255.255.0")	->	FALSE




.. _nxsl-gethostbyaddr:

gethostbyaddr
-------------

Under construction

.. _nxsl-gethostbyname:

gethostbyname
-------------

Under construction

Time-related
============

.. _nxsl-gmtime:

gmtime
------

Converts time in UNIX format (number of seconds since epoch) to calendar date and time broken down into its components, expressed as UTC (or GMT timezone). Function uses either time given in time argument or current time if time is omitted.


Syntax
~~~~~~

gmtime(time);


Parameters
~~~~~~~~~~



 time 
 Time as seconds since epoch (1 January 1970 00:00:00 UTC). If omitted, current time is used.


Return Value
~~~~~~~~~~~~

Object of class TIME.


Examples
~~~~~~~~

gmtime(time())->year	->	2012
gmtime()->year		->	2012




.. _nxsl-localtime:

localtime
---------

Converts time in UNIX format (number of seconds since epoch) to calendar date and time broken down into its components. Function uses either time given in time argument or current time if time is omitted.


Syntax
~~~~~~

localtime(time);


Parameters
~~~~~~~~~~



 time 
 Time as seconds since epoch (1 January 1970 00:00:00 UTC). If omitted, current time is used.


Return Value
~~~~~~~~~~~~

Object of class TIME.


Examples
~~~~~~~~

localtime(time())->year		->	2012
localtime()->year		->	2012




.. _nxsl-SecondsToUptime:

SecondsToUptime
---------------

Format system uptime in seconds as string in format "n days, hh:mm".


Syntax
~~~~~~

SecondsToUptime(seconds)


Parameters
~~~~~~~~~~



 seconds 
 Number of seconds.


Return Value
~~~~~~~~~~~~

System uptime in format "n days, hh:mm".


Examples
~~~~~~~~

SecondsToUptime(600)     -> "0 days, 00:10"




.. _nxsl-strftime:

strftime
--------

Formats a Unix timestamp, and returns a string according to given formatting rules.


Syntax
~~~~~~

strftime(string);


Parameters
~~~~~~~~~~



 string 
 Formatting string - see this for available options http://www.cplusplus.com/reference/ctime/strftime/


Return Value
~~~~~~~~~~~~

Formatted time as a string.


Examples
~~~~~~~~


strftime("%Y-%m-%d %H:%M", time())						->	2016-01-19 12:14
strftime("%Y-%m-%d %H:%M - timezone %Z - offset from UTC - %z", time())		->	2016-01-19 12:14 - timezone CET - offset from UTC - +0100




.. _nxsl-time:

time
----

Gets the system time.


Syntax
~~~~~~

time();


Return Value
~~~~~~~~~~~~

System time as number of seconds elapsed since midnight (00:00:00), January 1, 1970, coordinated universal time, according to the system clock (also known as UNIX time).




.. _nxsl-mktime:

mktime
------

Under construction

Cryptography
============

.. _nxsl-md5:

md5
---

Under construction

.. _nxsl-sha1:

sha1
----

Under construction

.. _nxsl-sha256:

sha256
------

Under construction

SNMP
====

.. _nxsl-CreateSNMPTransport:

CreateSNMPTransport
-------------------

Create new SNMP transport object for specific node. The node must support SNMP.


Since: 1.2.1


Syntax
~~~~~~

CreateSNMPTransport(node);


Parameters
~~~~~~~~~~



 node 
 Node object the transport must be created from.


Return Value
~~~~~~~~~~~~

Object of class SNMP_Transport or null on failure.


Examples
~~~~~~~~

transport = CreateSNMPTransport(FindObject("MYWORKPC"));    // Create SNMP transport for node MYWORKPC
if (transport == null)
    return -1; // Exit on failure



.. _nxsl-SNMPGet:

SNMPGet
-------

Get the object value from specific node with SNMP GET request. The node and all SNMP communication details defined by SNMP transport.


Since: 1.2.1


Syntax
~~~~~~

SNMPGet(transport,oid);


Parameters
~~~~~~~~~~



 transport 
 SNMP_Transport SNMP transport object.


 oid 
 SNMP object id.


Return Value
~~~~~~~~~~~~

Object of class SNMP_VarBind or NULL on failure.


Examples
~~~~~~~~

transport = CreateSNMPTransport(FindObject("MYWORKPC"));    // Create SNMP transport for node MYWORKPC
if (transport == null)
    return -1; // Failed to create SNMP transport, exit
oid = ".1.3.6.1.2.1.25.1.6.0";	// number of running processes
varbind = SNMPGet(transport, oid);
if (varbind == null)
    return -2; // Failed to issue SNMP GET request to MYWORKPC, exit
else
    trace(1, "SNMP GET ".varbind->name."=".varbind->value);



.. _nxsl-SNMPGetValue:

SNMPGetValue
------------

Get the object value from specific node with SNMP GET request. The node and all SNMP communication details defined by SNMP transport. This function is similar to SNMPGet but returns string instead of an SNMP_VarBind object.


Since: 1.2.1


Syntax
~~~~~~

SNMPGetValue(transport,oid);


Parameters
~~~~~~~~~~



 transport 
 SNMP_Transport SNMP transport object.


 oid 
 SNMP object id.


Return Value
~~~~~~~~~~~~

String with the value requested or NULL on failure.


Examples
~~~~~~~~

transport = CreateSNMPTransport(FindObject("MYWORKPC"));    // Create SNMP transport for node MYWORKPC
if (transport == null)
    return -1; // Failed to create SNMP transport, exit
oid = ".1.3.6.1.2.1.25.1.6.0";	// number of running processes
value = SNMPGetValue(transport, oid);
if (value == null)
    return -2; // Failed to issue SNMP GET request to MYWORKPC, exit
else
    trace(1, "SNMP GET ".oid."=".value);



.. _nxsl-SNMPSet:

SNMPSet
-------

Assign a specific value to the given SNMP object for the node. The node and all SNMP communication details defined by SNMP transport. 


Since: 1.2.1


Syntax
~~~~~~

SNMPSet(transport,oid,value,[data type]);


Parameters
~~~~~~~~~~



 transport 
 SNMP_Transport SNMP transport object.


 oid 
 SNMP object id to start walking from.


 value 
 Value to assign to oid.


 data type 
 SNMP data type (optional).


Return Value
~~~~~~~~~~~~

TRUE on success, FALSE in case of failure.


Examples
~~~~~~~~

	ret = SNMPSet(transport, oid, "192.168.0.1", "IPADDR");
	if (!ret)
	{
		trace(1,"SNMPSet failed");
		return -1;
	}



.. _nxsl-SNMPWalk:

SNMPWalk
--------

Get an array of the object values from specific node with SNMP WALK request. The node and all SNMP communication details defined by SNMP transport. 


Since: 1.2.1


Syntax
~~~~~~

SNMPWalk(transport,oid);


Parameters
~~~~~~~~~~



 transport 
 SNMP_Transport SNMP transport object.


 oid 
 SNMP object id to start walking from.


Return Value
~~~~~~~~~~~~

Array of SNMP_VarBind objects or NULL on failure.


Examples
~~~~~~~~

	transport = CreateSNMPTransport(FindObject("MYWORKPC"));
	if (transport == null)
            return -1;
	oid = ".1.3.6.1.2.1.25.4.2.1.2"; // Names of the running processes
	vars = SNMPWalk(transport, oid);
	if (vars == null)
            return -2; // SNMPWalk failed	
	foreach (v: vars) {
	    trace(1, "SNMP WALK ".v->name."=".v->value);		
	}



Agent
=====

.. _nxsl-AgentReadList:

AgentReadList
-------------

Under construction

.. _nxsl-AgentReadParameter:

AgentReadParameter
------------------

Read parameter's value directly from agent on given node.


Since: 1.2.6


Syntax
~~~~~~

AgentReadParameter(node, name);


Parameters
~~~~~~~~~~



 node 
 Node object.


 name 
 Parameter's name.


Return Value
~~~~~~~~~~~~

Value of given parameter on success and NULL on failure.


Examples
~~~~~~~~

 v = AgentReadParameter($node, "Agent.Version");
 trace(1, "Agent version is " . v);



.. _nxsl-AgentReadTable:

AgentReadTable
--------------

Under construction

Event Processing
================

.. _nxsl-FindAlarmById:

FindAlarmById
-------------

Find active (non-terminated) alarm by alarm ID.


Since: 2.0-M4


Syntax
~~~~~~

FindAlarmById(id)


Parameters
~~~~~~~~~~



 id 
 Alarm ID.


Return Value
~~~~~~~~~~~~

Alarm object or null if no such alarm exist.




.. _nxsl-FindAlarmByKey:

FindAlarmByKey
--------------

Find active (non-terminated) alarm by alarm key.


Since: 2.0-M4


Syntax
~~~~~~

FindAlarmByKey(key)


Parameters
~~~~~~~~~~



 key 
 Alarm key.


Return Value
~~~~~~~~~~~~

Alarm object or null if no such alarm exist.




.. _nxsl-GetEventParameter:

GetEventParameter
-----------------

Get value of event's named parameter.


Since: 1.1.4


Syntax
~~~~~~

GetEventParameter(event, parameterName)


Parameters
~~~~~~~~~~



 event 
 Event object, you can use predefined variable $event to refer to current event.


 parameterName 
 Parameter's name.


Return Value
~~~~~~~~~~~~

String value of requested parameter or null if no such parameter exist.


Examples
~~~~~~~~

GetNamedParameter($event, "ifName")	-> "eth0"
GetNamedParameter($event, "bad_name")	-> NULL




.. _nxsl-PostEvent:

PostEvent
---------

Post event on behalf of given node.


Since: 1.0.8


Syntax
~~~~~~

PostEvent(node, event, tag, ...);


Parameters
~~~~~~~~~~



 node 
 Node object to send event on behalf of.


 event 
 Event code or name (name can be used since 1.2.6).


 tag 
 User tag associated with event. Optional, can be leaved out or set to null.


 ... 
 0 or more event-specific parameters.


Return Value
~~~~~~~~~~~~

TRUE if event was posted successfully or FALSE if not.


Examples
~~~~~~~~

PostEvent($node, 100000)
PostEvent($node, 100000, "my tag", "param1", "param2")
PostEvent($node, "MY_EVENT_NAME", null, "param1")




.. _nxsl-SetEventParameter:

SetEventParameter
-----------------

Set value of event's named parameter.


Since: 1.1.4


Syntax
~~~~~~

SetEventParameter(event, parameterName, value)


Parameters
~~~~~~~~~~



 event 
 Event object, you can use predefined variable $event to refer to current event.


 parameterName 
 Parameter's name.


 value 
 New value.


Return Value
~~~~~~~~~~~~

None.


Examples
~~~~~~~~

SetEventParameter($event, "customParameter", "new value")




Situations
==========

.. _nxsl-FindSituation:

FindSituation
-------------

Find situation instance either by situation object name and instance name or by situation object ID and instance name (name search is case-insensetive).


Syntax
~~~~~~

FindSituation(id, instance);


Parameters
~~~~~~~~~~



 id 
 Situation object name or ID.


 instance 
 Situation instance.


Return Value
~~~~~~~~~~~~

Situation object with given ID or name on success or null on failure.


Examples
~~~~~~~~

FindSituation("my_situation", "my_instance")		-> valid_object
FindSituation(1, "my_instance")			-> valid_object
FindSituation("bad_situation_name", "my_instance")	-> NULL




.. _nxsl-GetSituationAttribute:

GetSituationAttribute
---------------------

Under construction

