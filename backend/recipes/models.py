from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from foodgram import constants as c
from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        max_length=c.INGREDIENT_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Ingredient name',
        help_text='Ingredient name',
    )
    measurement_unit = models.CharField(
        max_length=c.MEASUREMENT_UNIT_MAX_LENGTH,
        verbose_name='Ingredient measurement unit',
        help_text='Ingredient measurement unit',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'measurement_unit'),
                name='unique_ingredient',
            ),
        )

    def __str__(self):
        return f'{self.name} ({self.measurement_unit})'


class Tag(models.Model):
    name = models.CharField(
        max_length=c.TAG_NAME_MAX_LENGTH,
        verbose_name='Tag name',
        help_text='Tag name',
    )
    slug = models.SlugField(
        max_length=c.TAG_SLUG_MAX_LENGTH,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Slug contains restricted symbols. Please use only '
                    'letters, numbers and _ symbol',
        ), ],
        verbose_name='Tag slug',
        help_text='Tag slug',
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        max_length=c.RECIPE_NAME_MAX_LENGTH,
        verbose_name='Recipe name',
        help_text='Recipe name',
    )
    text = models.TextField(
        verbose_name='Recipe description',
        help_text='Recipe description',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=False,
        through='RecipeIngredient',
        related_name='recipes',
        verbose_name='Recipe ingredients',
        help_text='Recipe ingredients',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(
            c.COOKING_TIME_MIN,
            f'Can not be less than {c.COOKING_TIME_MIN} minute(s)'
        ),),
        verbose_name='Cooking time in minutes',
        help_text='Cooking time in minutes',
    )
    image = models.ImageField(
        blank=False,
        verbose_name='Recipe image',
        help_text='Recipe image',
        upload_to='media/recipes/',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Recipe author',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=False,
        through='RecipeTags',
        related_name='recipes',
        verbose_name='Recipe tags',
        help_text='Recipe tags',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Recipe'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_recipe',
        verbose_name='Ingredient'
    )
    amount = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(
            c.INGREDIENT_AMOUNT_MIN,
            f'Minimum amount is {c.INGREDIENT_AMOUNT_MIN}'
        ),),
        verbose_name='Amount',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ingredient amount'
        verbose_name_plural = 'Ingredient amounts'
        constraints = (
            models.UniqueConstraint(
                fields=('ingredient', 'recipe'),
                name='unique_recipe_ingredient',
            ),
        )

    def __str__(self):
        return f'Recipe {self.recipe} contains ingredient {self.ingredient}'


class RecipeTags(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='tag_list',
        verbose_name='Recipe'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='tag_recipe',
        verbose_name='Tag'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Recipe tag'
        verbose_name_plural = 'Recipe tags'

    def __str__(self):
        return f'Recipe {self.recipe} has tag {self.tag}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Favorite user',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Favorite recipe',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favorite_recipe'
            ),
        )

    def __str__(self):
        return f'Recipe {self.recipe} is among favorites of user {self.user}'


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='User',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Recipe',
    )

    class Meta:
        verbose_name = "Shopping list"
        verbose_name_plural = "Shopping lists"

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_shopping_list_recipe'
            ),
        )

    def __str__(self):
        return (
            f'Recipe {self.recipe} is in shopping list of user {self.user}'
        )
