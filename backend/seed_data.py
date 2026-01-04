from app import create_app, db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.tower import Tower
from app.models.unit import Unit

app = create_app()

with app.app_context():
    print("Seeding database...")
    
    # Create Admin User
    # Using 'gmail.com' assuming 'gmial.com' was a typo
    admin_email = 'adminMain@gmail.com'
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(
            name='Super Admin',
            email=admin_email,
            role='admin'
        )
        admin.set_password('111')
        db.session.add(admin)
        print(f"Created admin user: {admin_email}")
    
    # Create Amenities
    amenities_data = [
        {'name': 'Air Conditioning', 'icon': 'snowflake'},
        {'name': 'High-Speed Internet', 'icon': 'wifi'},
        {'name': 'In-Unit Washer/Dryer', 'icon': 'local_laundry_service'},
        {'name': 'Dishwasher', 'icon': 'kitchen'},
        {'name': 'Balcony', 'icon': 'balcony'},
        {'name': 'Hardwood Floors', 'icon': 'layers'},
        {'name': 'Walk-in Closet', 'icon': 'door_sliding'},
        {'name': 'Pet Friendly', 'icon': 'pets'},
        {'name': 'Gym Access', 'icon': 'fitness_center'},
        {'name': 'Pool Access', 'icon': 'pool'},
        {'name': 'Parking', 'icon': 'directions_car'},
        {'name': 'Concierge', 'icon': 'room_service'}
    ]
    
    amenities = []
    for data in amenities_data:
        amenity = Amenity.query.filter_by(name=data['name']).first()
        if not amenity:
            amenity = Amenity(name=data['name'], icon=data['icon'])
            db.session.add(amenity)
        amenities.append(amenity)
    
    # Create Tower
    tower = Tower.query.filter_by(name='Skyline Residences').first()
    if not tower:
        tower = Tower(
            name='Skyline Residences',
            address='123 Main St, Cityville',
            total_floors=20
        )
        db.session.add(tower)
    
    db.session.commit() # Commit to get IDs
    
    # Create Units
    units_data = [
        {'unit_number': '101', 'floor': 1, 'bedrooms': 1, 'bathrooms': 1, 'area_sqft': 650, 'monthly_rent': 1800, 'status': 'available', 'amenity_indices': [0, 1, 3, 10]},
        {'unit_number': '205', 'floor': 2, 'bedrooms': 2, 'bathrooms': 2, 'area_sqft': 950, 'monthly_rent': 2400, 'status': 'available', 'amenity_indices': [0, 1, 2, 3, 4, 10]},
        {'unit_number': '515', 'floor': 5, 'bedrooms': 3, 'bathrooms': 2, 'area_sqft': 1300, 'monthly_rent': 3200, 'status': 'available', 'amenity_indices': [0, 1, 2, 3, 4, 5, 8, 9, 10, 11]},
        {'unit_number': '310', 'floor': 3, 'bedrooms': 1, 'bathrooms': 1, 'area_sqft': 700, 'monthly_rent': 1900, 'status': 'available', 'amenity_indices': [0, 1, 6, 10]},
        {'unit_number': 'A-101', 'floor': 1, 'bedrooms': 2, 'bathrooms': 2, 'area_sqft': 1100, 'monthly_rent': 2600, 'status': 'available', 'amenity_indices': [0, 1, 2, 3, 4, 5, 6, 7]}
    ]
    
    for u_data in units_data:
        unit = Unit.query.filter_by(unit_number=u_data['unit_number']).first()
        if not unit:
            unit = Unit(
                tower_id=tower.id,
                unit_number=u_data['unit_number'],
                floor=u_data['floor'],
                bedrooms=u_data['bedrooms'],
                bathrooms=u_data['bathrooms'],
                area_sqft=u_data['area_sqft'],
                monthly_rent=u_data['monthly_rent'],
                status=u_data['status']
            )
            # Add amenities
            for idx in u_data['amenity_indices']:
                if idx < len(amenities):
                    unit.amenities.append(amenities[idx])
            db.session.add(unit)
            
    db.session.commit()
    print("Database seeded successfully!")
