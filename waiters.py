session = boto3.session.Session()
for resource_name in session.get_available_resources():
    resource = boto3.resource(resource_name)
    for sub_resource in retrieve_sub_resources(session, resource):
        waiters = sub_resource.meta.resource_model.waiters
        print(waiters)
        if waiters:
            service_waiter_model = session._session.get_waiter_model(resource_name)
            service_model = resource.meta.client.meta.service_model
            for waiter in waiters:
                model = service_waiter_model.get_waiter(waiter.waiter_name)
                operational_model = service_model.operation_model(model.operation)
                ignore_params = get_resource_ignore_params(waiter.params)
                print(ignore_params)
                public_methods = get_instance_public_methods(resource.meta.client.get_waiter(waiter.waiter_name))