from math import ceil

#Daily Challenge : Pagination

class Pagination:
    def __init__(self, items = None, pageSize = 10) -> None:
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
    def getVisibleItems(self):
        list_visible = []
        the_range = min((self.pageSize*self.currentPage), len(self.items))
        lower_Border = (self.pageSize*self.currentPage)-(self.pageSize)
        for i in range(lower_Border, the_range):
            list_visible.append(self.items[i])
        return list_visible
    def prevPage(self):
        if self.currentPage == 1:
            print("This is the first page")
        else:
            self.currentPage -= 1
    def nextPage(self):
        if (self.currentPage * self.pageSize >= len(self.items)):
            print("This is the last page")
        else:
            self.currentPage += 1
    def firstPage(self):
        self.currentPage = 1
    def lastPage(self):
        self.currentPage = ceil(len(self.items) / self.pageSize)
    def goToPage(self, pageNum):
        if (pageNum > int(len(self.items) / self.pageSize)):
            print(f"There is no page {pageNum}")
            return
        self.currentPage = int(pageNum)

book = Pagination("qwertyasdfghzxcvbnm", 3)
print("first page")
print(book.getVisibleItems())
print("previous page")
book.prevPage()
print(book.getVisibleItems())
print("first page")
book.firstPage()
print(book.getVisibleItems())
print("last page")
book.lastPage()
print(book.getVisibleItems())
print("previous page")
book.prevPage()
print(book.getVisibleItems())
print("next page")
book.nextPage()
print(book.getVisibleItems())
print("next page")
book.nextPage()
print(book.getVisibleItems())
print("go to page 5")
book.goToPage(5)
print(book.getVisibleItems())
print("go to page 9")
book.goToPage(9)
print(book.getVisibleItems())