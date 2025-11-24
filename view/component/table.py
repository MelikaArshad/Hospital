
import tkinter.ttk as ttk


class Table:
    def __init__(self, window, headings, column_widths, x, y, height=10, function_name=None):
        self.function_name = function_name
        columns = list(range(len(headings)))

        self.table = ttk.Treeview(window, columns=columns, height=height, show="headings")

        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=column_widths[col])

        # Calculate scrollbar position (to the right of the table)
        scrollbar_x = x + sum(column_widths)

        self.table.place(x=x, y=y)

        # Get the actual height of the treeview
        table_height = self.table.winfo_reqheight()

        # Create vertical scrollbar with matching height
        self.scrollbar = ttk.Scrollbar(window, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=scrollbar_x, y=y, height=table_height)

        self.table.bind("<<TreeviewSelect>>", self.table_select)

    # def __init__(self,window,headings,column_widths,x,y,height=10,function_name=None):
    #     columns = list(range(len(headings)))
    #     self.table=ttk.Treeview(window,columns=columns,height=height,show='headings')
    #     self.table.place(x=x,y=y)
    #     for col,text in enumerate(headings):
    #         self.table.heading(col,text=text)
    #         self.table.column(col,width=column_widths[col])
    #     if function_name:
    #         self.table.bind("<<TreeviewSelect>>",self.table_select)
    #         self.function=function_name
    def table_select(self, _):
        row_id = self.table.focus()
        if row_id:
            item = self.table.item(row_id)
            if item["values"] and self.function_name:
                self.function_name(item["values"])

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def refresh_table(self, data_list):
        self.clear_table()
        if data_list:
            for data in data_list:
                if hasattr(data,"to_tuple"):
                    values=data.to_tuple()
                else:
                    values=tuple(data)

                self.table.insert("", "end", values=values)


