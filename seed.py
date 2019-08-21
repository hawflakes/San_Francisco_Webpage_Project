import datetime
from sqlalchemy import func

#from model import User, connect_to_db, db, Neighborhood, Restaurant_reaction, Place, Place_comment
from model import *

from server import app


def load_users():
    """Load sample users into database."""

    liz = User(fname="Liz", lname="Law", email="liz@gmail.com", password="donut", status="resident")
    ash = User(fname="Ash", lname="Ma", email="ash@gmail.com", password="lashes", status="resident")
    tk = User(fname="Tk", lname="Kombarov", email="tk@gmail.com", password="kz", status="resident")
    jess = User(fname="Jess", lname="Ho", email="jess@gmail.com", password="python", status="resident")
    chad = User(fname="Chad", lname="Bradley", email="chad@gmail.com", password="ebitda", status="visitor")
    rachel = User(fname="Rachel", lname="Wang", email="rachel@gmail.com", password="jellyfish", status="visitor")
    jon = User(fname="Jon", lname="Whiteaker", email="jon@gmail.com", password="square", status="resident")

    for user in [liz,ash,tk,jess,chad,rachel, jon]:
        db.session.add(user)

    db.session.commit()


def load_neighborhoods(neighborhood_filename):
    """Load nighborhoods from u.neighborhoodinto database."""

    for i, row in enumerate(open(neighborhood_filename)):
        row = row.rstrip()

        # unpack the row
        neighborhood_id, name, description, img_path = row.split("|")

        neighborhood = Neighborhood(neighborhood_id=neighborhood_id,
                                    name=name,
                                    description=description,
                                    image_url=img_path)


        db.session.add(neighborhood)

    db.session.commit()

def load_places_to_visit(places_filename):
    """Load places from u.place into database."""

    for i, row in enumerate(open(places_filename)):
        row = row.rstrip()

        # unpack the row
        place_id, name, neighborhood_id, description, p_lat, p_long, img_path = row.split("|")

        place = Place(place_id=place_id,
                        name=name,
                        neighborhood_id=neighborhood_id,
                        description=description,
                        p_lat=p_lat,
                        p_long=p_long,
                        image_url=img_path)


        db.session.add(place)

    db.session.commit()


def load_restaurant_reactions(rest_reaction_filename):
    """Load reactions from u.rest_comments into database."""

    for i, row in enumerate(open(rest_reaction_filename)):
        row = row.rstrip()

        # unpack the row
        user_id, comment, created_date, neighborhood_id = row.split("|")
  
        create_date = datetime.strptime(created_date, "%b %d, %Y")
    

        r_comment = Restaurant_reaction(user_id=user_id,
            comment=comment, created_date=create_date, neighborhood_id=neighborhood_id)

        

        db.session.add(r_comment)

    db.session.commit()


def load_place_comments(place_comments_filename):
    """Load places from u.place_comments into database."""

    for i, row in enumerate(open(place_comments_filename)):
        row = row.rstrip()

        # unpack the row
        user_id, place_id, comment, created_date, rating = row.split("|")

        create_date = datetime.strptime(created_date, "%b %d, %Y")

        p_comment = Place_comment(user_id=user_id, place_id=place_id,
            comment=comment, created_date=create_date, rating=rating)
        

        db.session.add(p_comment)

    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all() #prevents dupe seeding
    db.create_all()

    neighborhood_filename = "seed_data/u.neighborhood"
    places_filename = "seed_data/u.place"
    rest_reaction_filename = "seed_data/u.rest_comments"
    place_comments_filename = "seed_data/u.place_comments"


    load_users()
    load_neighborhoods(neighborhood_filename)
    load_places_to_visit(places_filename)
    load_restaurant_reactions(rest_reaction_filename)
    load_place_comments(place_comments_filename)

    

