


def _hashtag(txt='',*args,**kwargs):
    """ 
    this function will take in a sting and return
    an array containing non repeating starting
    with hashtags

    txt must be a string
    """
    txt=str(txt)
    txt=txt.title().strip(' ,')
    tags=txt.split(',')
    return tags



def _unique_list(arr=[]):
    """
    this function takes in array of items as argument and
    return and array of the item without duplicate
    """
    return list(set(arr))



def _all_post_tag(model=[]):
    """
    this function iterate through all the post models
    and get all the tag available.
    the function takes in model.objects.all() as argument
    """
    all_tag=[]
    for m in model:
        all_tag+=_hashtag(txt=m.tags)

    return _unique_list(arr=all_tag)

        

