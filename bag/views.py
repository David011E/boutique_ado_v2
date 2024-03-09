from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Create a session so user can browse the store and the items will remain in the bag
    bag = request.session.get('bag', {}) # Will get the bag variable if exists in session if not create it 

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity      # Add the item to the bag or update the quantity if already exists
    
    request.session['bag'] = bag     # then over write the variable in the session with the updated session

    return redirect(redirect_url)