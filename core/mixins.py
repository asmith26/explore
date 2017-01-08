

class PageMixin(object):
    page = ""
    
    def get_context_data(self, *args, **kwargs):
        kwargs["page"] = self.page
        return super(PageMixin, self).get_context_data(*args, **kwargs)