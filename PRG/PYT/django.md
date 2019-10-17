Django
============

## Model and Form

### XXX\_set
When model A has foreign keys to model B, B has an attribute `A_set` that has a set of A instances whose foreign key is to the instance. `A_set` has also a method `craete()`.

### Safe filter
To escape all the HTML symbols. https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#safe

### Cleaning and validation
The correct process is `clean()` -> `is_valid()`.

Validation can be tested easily like this:
```python
 def test_user_valid_clean_success(self):
        form_data = {
                'username' : 'john',
                'password' : 'john',
                're_password' : 'john',}
        form = UserCreationForm(data=form_data)
        
        self.assertEqual(form.is_valid(),True)
```

## Testing

### Client
TestCase in `django` has a client instnace.

### Use setUpTestData instaed of setUpClass
The document says.


## Fuctions

### Backup
[dumpdate](https://docs.djangoproject.com/en/2.2/ref/django-admin/#dumpdata).



