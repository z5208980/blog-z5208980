---
title: "2 Digit Year Formatting"
date: "2022-08-01"
tags: ["C#", "Developer"]
image: ""
gradients: ["#d558c8", "#24d292"]
---

## CultureInfo

`System.Globalization.CultureInfo.InvariantCulture` is the default configuration where I guess their values `Calendar.TwoDigitYearMax` is basic of ** Customize Format** in Window 10 settings. This can be access via `Control Panel > Clock and Region > Change date, time and Number Formats`. Under the `Format Setting` *Additional Setting* Button where it'll take you to **Customize Format**. In the Date tab there should be a **Calender** section that allows the user to change the two-digit years. 

To customise this in C# we can set our own `CultureInfo` Class that sets `Calendar.TwoDigitYearMax` value and use it in the `ParseDateTime()` or `TryParse()` method. This requires the assembly `System.Globalisation`.

```csharp
using System;
using System.Globalization;

public class Program
{
	public static void Main()
	{
		CultureInfo ci = new CultureInfo(CultureInfo.CurrentCulture.LCID);
		ci.Calendar.TwoDigitYearMax = 2023;

		var dateString = "5/1/23 8:30:52 AM";
		//object obj = DateTime.Parse(dateString, System.Globalization.CultureInfo.InvariantCulture);
		object obj = DateTime.Parse(dateString, ci);

		DateTime value = DateTime.MinValue;
		if (obj != null && obj != DBNull.Value)
		DateTime.TryParse(dateString, ci, DateTimeStyles.None, out value);
		
		Console.WriteLine(value.ToString());
	}
}
```

In this case, we set a `CultureVariant` with a `TwoDigitYearMax` of **2023**. This will overwrite the default system setting in Control Panel. Now year `24` will be interpreted to 1924 rather than 2024 and setting `23` and **less** will result in the 21th Century. The reason why this may be important in order to control the systems of Date Time within the C# project or in cases where the code interacts with different OS systems that may have different implementation of two digit years.