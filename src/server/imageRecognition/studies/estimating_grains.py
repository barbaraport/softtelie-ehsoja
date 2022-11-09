from math import floor

AVERAGE_CM_POD_DIAMETER = 1.5

def main():
    plant_size_cm = int(input("Tamanho da planta, em centímetros: ")) # 150 cm
    plant_size_px = int(input("Tamanho da planta, em pixels: ")) # maybe it can be the size from the image or the bounding box from the soy plant (train another model to recognize it)

    bboxes = [[163, 433, 209, 461], # mocked bboxes
       [498, 438, 531, 466],
       [539, 507, 572, 527],
       [403, 423, 429, 457],
       [308, 456, 354, 508],
       [310, 394, 336, 426],
       [218, 396, 256, 423]]

    cm_per_pixel = get_cm_per_pixel(plant_size_cm, plant_size_px)
    print("Centímetros por pixel: ", cm_per_pixel)

    bboxes_shape = get_bboxes_shape(bboxes)
    print("Tamanho das bboxes em pixels: ", bboxes_shape)

    pods_sizes = get_pods_real_size(bboxes_shape, cm_per_pixel)
    print("Tamanho das vagens em centímetros: ", pods_sizes)

    seed_quantity = get_soy_seeds_per_pod(pods_sizes)
    print("Quantidade de grãos: ", seed_quantity)


def get_cm_per_pixel(plant_size_cm, plant_size_px):
    cm_per_pixel = plant_size_cm / plant_size_px

    return cm_per_pixel


def get_bboxes_shape(bboxes):

    shapes = []
    
    for bbox in bboxes:
        y1, x1, y2, x2 = bbox

        shape1 = abs(y1 - y2)
        shape2 = abs(x1 - x2)

        pod_shape = [shape1, shape2]

        height = max(pod_shape)
        width = min(pod_shape)

        pod_shape = [height, width]

        shapes.append(pod_shape)

    return shapes


def get_pods_real_size(shapes, cm_per_pixel):
    sizes = []
    
    for shape in shapes:
        height, width = shape

        real_height = height * cm_per_pixel
        real_width = width * cm_per_pixel

        real_shape = [real_height, real_width]

        sizes.append(real_shape)

    return sizes


def get_soy_seeds_per_pod(pods_sizes):

    seeds_quantity = 0

    for pod_size in pods_sizes:
        
        height, _ = pod_size
        pod_seeds = floor(height / AVERAGE_CM_POD_DIAMETER)

        seeds_quantity += pod_seeds

    return seeds_quantity


main()
