import attrs
import time
@attrs.define
class TesClass:
    heavy_second_function: bool = attrs.field(repr=True)
    first_method_time_out:float=attrs.field(default=0.5)
    seccond_method_time_out: float = attrs.field(default=0.25)
    third_method_time_out: float = attrs.field(default=1)
    number_of_iterations:int = attrs.field(default=5)


    def first_method(self):
        time.sleep(self.first_method_time_out)
    def second_method(self):
        time.sleep(self.seccond_method_time_out+(3 if self.heavy_second_function else 0))
    def third_method(self):
        time.sleep(self.third_method_time_out)
    def RunMe(self):
        for iteration in range(self.number_of_iterations):
            print(f"iteration {iteration}")
            print("Method 1")
            self.first_method()
            print("Method 2")

            self.second_method()
            print("Method 3")

            self.third_method()