from django.contrib import admin
from .models import Category, Comment, Product, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configure the category model for the Djiango admin interface.
    """
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}


#  Registration my Product-tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Configure the tag model for the Django admin interface.
    Attributes:
        list_display: Fields displayed in the tag list.
    """
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configure the product model for the Django admin interface.
    """
    list_display = ("name", "category", "price", "average_rating", "rating_count", "created_at")
    list_select_related = ("category",)

    #  here is added my filter
    list_filter = ("category", "tags")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configure the comment model for the Djiango admin interface.
    """
    list_display = ("product", "user", "guest_name", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("guest_name", "guest_email", "text", "user__username")
