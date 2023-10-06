from django.shortcuts import render
from .models import Book, BookInstance, Genre, Author, Language
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_bookinstances = BookInstance.objects.all().count()
    num_bookinstances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {'num_books': num_books, 
               'num_bookinstances': num_bookinstances,
               'num_bookinstances_available': num_bookinstances_available,
               'num_authors': num_authors,
               'num_visits': num_visits,
               }
    
    return render(request, 'index.html', context)


from django.views import generic

# 創建書本的列表跟詳細說明視圖
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
class BookDetailView(generic.DetailView):
    model = Book
    
# 創建作者列表跟作者詳細資料的視圖
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    
class AuthorDetailView(generic.DetailView):
    model = Author
    
    
# 創建借閱者的視圖
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_absoult_url(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').oder_by('due_back')
    

from django.contrib.auth.mixins import PermissionRequiredMixin

class LibraryStaffPermissionView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_permission.html'
    paginate_by = 10
    
    permission_required = 'catalog.can_mark_returned'
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
    
    
# 創建修改租借日期的視圖
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renew_date']
            book_inst.save()
            
            return HttpResponseRedirect(reverse('all-borrowed'))
        
    else:
        proposed_renew_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renew_date': proposed_renew_date})

    context = {'form': form, 'bookinst': book_inst}

    return render(request, 'catalog/book_renew_librarian.html', context)


# 創建作者的視圖
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'2020/05/01',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    
    
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
class BookUpdate(DeleteView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')