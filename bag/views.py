from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Create a session so user can browse the store and the items will remain in the bag
    bag = request.session.get('bag', {}) # Will get the bag variable if exists in session if not create it 

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():     # Check if same id and same size already exists
                bag[item_id]['items_by_size'][size] += quantity     # if it does increment the quantity for that size 
            else:
                bag[item_id]['items_by_size'][size] = quantity  
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    else: # if there is no size run this logic
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity      # Add the item to the bag or update the quantity if already exists
            
    request.session['bag'] = bag     # then over write the variable in the session with the updated session
   

    return redirect(redirect_url)